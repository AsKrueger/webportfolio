/** Filas, columnas y las dos diagonales, en ese orden. */
fun BoardSize.lines(): List<Line> {
    val n = dimension
    val range = 0 until n
    return range.map { row -> Line(LineType.ROW, row, range.map { column -> row * n + column }) } +
        range.map { column -> Line(LineType.COLUMN, column, range.map { row -> row * n + column }) } +
        Line(LineType.DIAGONAL, 0, range.map { it * (n + 1) }) +
        Line(LineType.DIAGONAL, 1, range.map { (it + 1) * (n - 1) })
}

fun Board.completedLines(): List<Line> = size.lines().filter { line -> line.cells.all { goals[it].isCompleted } }

/** Bingo: todas las casillas cumplidas. */
val Board.isFullCard: Boolean get() = goals.all { it.isCompleted }

/** Qué hay que celebrar tras un cambio. */
sealed interface Celebration {
    data object None : Celebration

    /** Una o más líneas nuevas, para tacharlas con el rotulador. */
    data class Lines(val lines: List<Line>) : Celebration

    data object Bingo : Celebration
}

/** Lo nuevo que hay que celebrar al pasar de `before` a `after`. */
fun celebrationBetween(before: Board, after: Board): Celebration {
    if (after.isFullCard) return if (before.isFullCard) Celebration.None else Celebration.Bingo
    val previous = before.completedLines().toSet()
    val fresh = after.completedLines().filterNot { it in previous }
    return if (fresh.isEmpty()) Celebration.None else Celebration.Lines(fresh)
}
