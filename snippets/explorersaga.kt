suspend fun sync(): SyncResult = withContext(Dispatchers.IO) {
    try {
        val manifest = ContentImporter.json.decodeFromString<ContentManifest>(
            download(baseUrl + MANIFEST).decodeToString()
        )
        if (manifest.schema != ContentImporter.SUPPORTED_SCHEMA) return@withContext SyncResult.UP_TO_DATE
        if (manifest.version <= (dao.meta()?.version ?: 0)) return@withContext SyncResult.UP_TO_DATE

        val bytes = download(baseUrl + manifest.file)
        if (bytes.size.toLong() != manifest.size || ContentImporter.sha256(bytes) != manifest.sha256) {
            Log.w(TAG, "Paquete descartado: tamaño o hash no coinciden")
            return@withContext SyncResult.FAILED
        }
        importMutex.withLock {
            import(ContentImporter.readPack(ByteArrayInputStream(bytes)))
        }
        SyncResult.UPDATED
    } catch (e: IOException) {
        Log.w(TAG, "No se pudo actualizar el contenido", e)
        SyncResult.FAILED
    } catch (e: IllegalArgumentException) {
        Log.w(TAG, "Paquete de contenido no válido", e)
        SyncResult.FAILED
    }
}
