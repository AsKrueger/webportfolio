enum class DataSourceOrigin {
    REMOTE,
    LOCAL_FALLBACK,
    NONE
}

data class PlacesResult(
    val places: List<PlaceEntity>,
    val origin: DataSourceOrigin
)

// Room es la única caché local: refleja la última sincronización correcta con el backend
// o, si nunca la hubo, los lugares incluidos en la app
class PlaceRepository(
    private val placeDao: PlaceDao,
    private val api: ExplorerSagaApi,
    private val importApi: ExplorerSagaApi,
    private val loadBundledPlaces: () -> List<PlaceEntity>
) {

    // …
    suspend fun getPlacesResult(): PlacesResult = withContext(Dispatchers.IO) {
        val remotePlaces = try {
            api.getPlaces()
        } catch (e: Exception) {
            e.printStackTrace()
            emptyList()
        }

        if (remotePlaces.isEmpty()) {
            return@withContext PlacesResult(getCachedPlaces(), DataSourceOrigin.LOCAL_FALLBACK)
        }

        val entities = remotePlaces.map { it.toPlaceEntity() }
        try {
            placeDao.replaceAll(entities)
        } catch (e: Exception) {
            e.printStackTrace()
        }
        PlacesResult(entities, DataSourceOrigin.REMOTE)
    }
    // …
}
