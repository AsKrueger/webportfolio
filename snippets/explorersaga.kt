enum class DataSourceOrigin {
    REMOTE,
    LOCAL_FALLBACK,
    NONE
}

data class PlacesResult(
    val places: List<PlaceEntity>,
    val origin: DataSourceOrigin
)

class PlaceRepository(private val context: Context) {

    private val json = Json { ignoreUnknownKeys = true }

    suspend fun getPlacesResult(category: String? = null): PlacesResult = withContext(Dispatchers.IO) {
        try {
            val remotePlaces = RetrofitClient.api.getPlaces(category)
            if (remotePlaces.isNotEmpty()) {
                PlacesResult(remotePlaces.map { it.toPlaceEntity() }, DataSourceOrigin.REMOTE)
            } else {
                val localPlaces = loadPlacesFromAssets()
                val filteredLocal = if (category != null) localPlaces.filter { it.category.contains(category, ignoreCase = true) } else localPlaces
                PlacesResult(filteredLocal, DataSourceOrigin.LOCAL_FALLBACK)
            }
        } catch (e: Exception) {
            e.printStackTrace()
            val localPlaces = loadPlacesFromAssets()
            val filteredLocal = if (category != null) localPlaces.filter { it.category.contains(category, ignoreCase = true) } else localPlaces
            PlacesResult(filteredLocal, DataSourceOrigin.LOCAL_FALLBACK)
        }
    }
    // …
}
