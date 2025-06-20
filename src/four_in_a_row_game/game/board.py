# --- Windsurf Metadata ---
# Assistant: core_game_logic
# Created: 2025-06-20
# Modified: 2025-06-20
# --- End Windsurf Metadata ---
"""Board representation and game-rule logic for 4-in-a-row.

This module provides an immutable `BoardState` dataclass that represents the
current grid and exposes helper methods to:

* Drop a piece in a column (returning a *new* BoardState)
* Detect win / draw conditions
* Query board fullness / valid moves

The implementation purposefully avoids any rendering or pygame references so
it can be unit-tested in isolation and reused by AI modules.
"""
from __future__ import annotations

from dataclasses import dataclass, replace
from typing import Iterable, Optional, Tuple

from four_in_a_row_game.core.constants import (
    DEFAULT_BOARD_COLS,
    DEFAULT_BOARD_ROWS,
    DEFAULT_CONNECT_LENGTH,
    DIRECTIONS,
    GameResult,
    PieceType,
)
from four_in_a_row_game.core.exceptions import InvalidMoveError

# Type alias for coordinates (row, col)
Coord = Tuple[int, int]


def _create_empty_grid(rows: int = DEFAULT_BOARD_ROWS, cols: int = DEFAULT_BOARD_COLS) -> Tuple[Tuple[PieceType, ...], ...]:
    """Return a rows×cols tuple-of-tuples initialised with PieceType.EMPTY."""
    return tuple(tuple(PieceType.EMPTY for _ in range(cols)) for _ in range(rows))


@dataclass(frozen=True, slots=True)
class BoardState:
    """Immutable board state.

    Attributes
    ----------
    grid
        A tuple-of-tuples storing the cell values. Indexing order is ``grid[row][col]``
        with (0,0) at the top-left.
    current_player
        Which player is next to move.
    last_move
        Coordinates of the last played piece (row, col) or ``None`` if no move
        has been made yet.
    connect_length
        Number of consecutive pieces required to win (default 4).
    """

    grid: Tuple[Tuple[PieceType, ...], ...] = _create_empty_grid()
    current_player: PieceType = PieceType.PLAYER_1
    last_move: Optional[Coord] = None
    connect_length: int = DEFAULT_CONNECT_LENGTH

    # ---------------------------------------------------------------------
    # Helper construction methods
    # ---------------------------------------------------------------------
    @classmethod
    def new(cls, rows: int = DEFAULT_BOARD_ROWS, cols: int = DEFAULT_BOARD_COLS) -> "BoardState":
        """Return a fresh empty board with the given dimensions."""
        return cls(grid=_create_empty_grid(rows, cols))

    # ------------------------------------------------------------------
    # Core game-logic operations
    # ------------------------------------------------------------------
    def drop_piece(self, column: int) -> "BoardState":
        """Return a **new** BoardState with the current player's piece dropped.

        Raises
        ------
        InvalidMoveError
            If the column index is out of range or the column is already full.
        """
        rows = len(self.grid)
        cols = len(self.grid[0])

        if not 0 <= column < cols:
            raise InvalidMoveError(f"Column {column} is out of range (0-{cols - 1})")

        # Find the lowest empty row in the column
        target_row = None
        for row in reversed(range(rows)):
            if self.grid[row][column] == PieceType.EMPTY:
                target_row = row
                break
        if target_row is None:
            raise InvalidMoveError(f"Column {column} is full")

        # Build a new grid with the piece placed
        new_grid = [list(r) for r in self.grid]  # mutable copy
        new_grid[target_row][column] = self.current_player
        frozen_grid = tuple(tuple(r) for r in new_grid)

        # Switch player turn
        next_player = (
            PieceType.PLAYER_2 if self.current_player == PieceType.PLAYER_1 else PieceType.PLAYER_1
        )

        return replace(self, grid=frozen_grid, current_player=next_player, last_move=(target_row, column))

    # ------------------------------------------------------------------
    # Query helpers
    # ------------------------------------------------------------------
    def winner(self) -> GameResult:
        """Return the game result from the *current* grid.

        * ``GameResult.WIN_PLAYER_X`` – X is the *previous* mover (uses ``last_move``)
        * ``GameResult.DRAW`` – board full with no winner
        * ``GameResult.ONGOING`` – otherwise
        """
        # No move yet – cannot be a win
        if self.last_move is None:
            return GameResult.ONGOING

        last_row, last_col = self.last_move
        last_piece = self.grid[last_row][last_col]

        # Iterate directions and count consecutive pieces including last move
        for dr, dc in DIRECTIONS:
            count = 1  # include last piece
            # Look in the positive direction
            count += self._count_aligned(last_row, last_col, dr, dc, last_piece)
            # And the negative opposite direction
            count += self._count_aligned(last_row, last_col, -dr, -dc, last_piece)
            if count >= self.connect_length:
                return (
                    GameResult.WIN_PLAYER_1
                    if last_piece == PieceType.PLAYER_1
                    else GameResult.WIN_PLAYER_2
                )

        # Check draw
        if self.is_full():
            return GameResult.DRAW

        return GameResult.ONGOING

    def is_full(self) -> bool:
        """Return ``True`` if no empty cells remain."""
        return all(cell != PieceType.EMPTY for row in self.grid for cell in row)

    # ------------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------------
    def _count_aligned(self, row: int, col: int, dr: int, dc: int, piece: PieceType) -> int:
        """Count consecutive pieces from (row, col) in (dr, dc) direction."""
        rows = len(self.grid)
        cols = len(self.grid[0])
        r, c = row + dr, col + dc
        count = 0
        while 0 <= r < rows and 0 <= c < cols and self.grid[r][c] == piece:
            count += 1
            r += dr
            c += dc
        return count

    # ------------------------------------------------------------------
    # Convenience representations
    # ------------------------------------------------------------------
    def __str__(self) -> str:  # pragma: no cover – debug helper
        symbols = {PieceType.EMPTY: ".", PieceType.PLAYER_1: "X", PieceType.PLAYER_2: "O"}
        lines = ["".join(symbols[cell] for cell in row) for row in self.grid]
        return "\n".join(lines)


__all__: Iterable[str] = [
    "BoardState",
]
