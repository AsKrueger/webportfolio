/**
 * Turns training into XP, levels and stats. Everything is deterministic and pure, so the totals
 * can always be rebuilt from the stored workouts.
 */
object RpgEngine {
    // …

    /** XP needed to go from [level] to the next one. */
    fun xpToNextLevel(level: Int): Long = (100 * level.toDouble().pow(1.5)).roundToInt().toLong()

    /**
     * The reward for a finished workout.
     * @param streakWeeks consecutive weeks with training before this workout.
     * @param restedBefore whether there was at least one rest day since the previous workout.
     */
    fun reward(
        sets: List<SetForReward>,
        heroClass: HeroClass?,
        bodyweightKg: Double,
        streakWeeks: Int,
        restedBefore: Boolean,
    ): WorkoutReward {
        val stats = Stat.entries.associateWith { 0.0 }.toMutableMap()
        var xp = 0.0
        sets.forEach { (profile, set, isPr) ->
            var setXp = setXp(set, bodyweightKg)
            if (setXp == 0.0) return@forEach
            if (isPr) setXp *= PR_MULTIPLIER
            val weights = statWeights(profile, set.reps)
            val main = weights.maxBy { it.value }.key
            if (heroClass != null && main in heroClass.focus) setXp *= heroClass.bonus
            xp += setXp
            weights.forEach { (stat, weight) -> stats[stat] = stats.getValue(stat) + setXp * weight / 10 }
        }
        if (xp == 0.0) return WorkoutReward(0, stats)
        val streakMultiplier = 1 + 0.05 * streakWeeks.coerceIn(0, 4)
        stats[Stat.DIS] = stats.getValue(Stat.DIS) + 3 + streakWeeks.coerceIn(0, 10) * 0.5
        if (restedBefore) stats[Stat.REC] = stats.getValue(Stat.REC) + 2
        val total = ((xp + COMPLETION_BONUS) * streakMultiplier).roundToInt()
        return WorkoutReward(total, stats)
    }
}
