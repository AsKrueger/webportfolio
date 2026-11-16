/**
 * The anime airing now, kept in a file. Loading them takes about fifteen requests to Kitsu, so the
 * calendar shows the saved copy at once and only asks again when that copy is a few hours old.
 */
class AiringRepository(
    private val catalog: AnimeCatalog,
    private val file: File,
    private val json: Json,
    private val now: () -> Long = System::currentTimeMillis,
) {
    @Serializable
    private data class Snapshot(val savedAt: Long, val animes: List<Anime>)

    /** The saved copy, however old, or null when there is none or it can't be read. */
    suspend fun cached(): CachedAiring? = withContext(Dispatchers.IO) {
        try {
            if (!file.exists()) return@withContext null
            val snapshot = json.decodeFromString<Snapshot>(file.readText())
            CachedAiring(snapshot.animes, fresh = now() - snapshot.savedAt < MAX_AGE_MS)
        } catch (_: IOException) {
            null
        } catch (_: SerializationException) {
            null
        } catch (_: IllegalArgumentException) {
            null
        }
    }

    /** Asks Kitsu again and replaces the saved copy. Throws [IOException] without a connection. */
    suspend fun fetch(): List<Anime> {
        val animes = catalog.airing()
        withContext(Dispatchers.IO) {
            try {
                val temp = File(file.parentFile, "${file.name}.tmp")
                temp.writeText(json.encodeToString(Snapshot(now(), animes)))
                temp.renameTo(file)
            } catch (_: IOException) {
                // Not saving only means the next visit loads from the network again.
            }
        }
        return animes
    }

    // …

    private companion object {
        const val MAX_AGE_MS = 6L * 60 * 60 * 1000
    }
}
