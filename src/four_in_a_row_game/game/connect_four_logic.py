# --- Windsurf Metadata ---
# Assistant: core_game_logic
# Created: 2025-06-20
# Modified: 2025-06-20
# --- End Windsurf Metadata ---
"""Game-specific logic for standard Connect Four variant.

This class plugs into ``core.game_engine.GameLogic`` protocol and wraps the
immutable ``BoardState`` to provide gameplay operations and integration with
pygame input events.

The design keeps gameplay rules separate from rendering so it can be unit-
tested in isolation. For now we only support local human-vs-human play; AI and
network play can be added later.
"""
from __future__ import annotations

from typing import List

import pygame

from four_in_a_row_game.core.constants import GameResult, GameState, PieceType
from four_in_a_row_game.game.board import BoardState
from four_in_a_row_game.core.exceptions import InvalidMoveError
from four_in_a_row_game.config.game_settings import GameSettings


class ConnectFourLogic:
    """Connect-Four gameplay controller implementing the GameLogic protocol."""

    def __init__(self, config: GameSettings):
        self.settings = config
        self.board: BoardState = BoardState.new(
            rows=config.board_height, cols=config.board_width
        )
        self.result: GameResult = GameResult.ONGOING
        self.game_state_enum = GameState.PLAYING

    # ------------------------------------------------------------
    # Public helpers (useful for tests / CLI)
    # ------------------------------------------------------------
    def make_move(self, column: int) -> None:
        """Attempt to drop a piece for the current player in *column*."""
        if self.result != GameResult.ONGOING:
            return
        try:
            self.board = self.board.drop_piece(column)
        except InvalidMoveError as exc:
            # Ignore invalid move for now – UI can surface message
            raise InvalidMove(str(exc))
        self._update_result()

    # ------------------------------------------------------------
    # GameLogic protocol implementation
    # ------------------------------------------------------------
    def handle_input(
        self, events: List[pygame.event.Event], game_state: "GameState"
    ) -> None:  # noqa: D401 – protocol signature
        """Translate mouse clicks to column moves."""
        for evt in events:
            if evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1:
                # Simple mapping: divide window width evenly by columns
                window_width = self.settings.window_width
                col_width = window_width / self.settings.board_width
                column = int(evt.pos[0] // col_width)
                try:
                    self.make_move(column)
                except InvalidMove:
                    pass  # invalid moves are silently ignored for now

    def update(self, dt: float, game_state: "GameState") -> None:  # noqa: D401
        # No per-frame logic needed yet
        pass

    def is_game_over(self, game_state: "GameState") -> bool:  # noqa: D401
        return self.result != GameResult.ONGOING

    # ------------------------------------------------------------
    # Internal helpers
    # ------------------------------------------------------------
    def _update_result(self) -> None:
        self.result = self.board.winner()

    # ------------------------------------------------------------
    # Debug helpers
    # ------------------------------------------------------------
    def __str__(self) -> str:  # pragma: no cover
        return str(self.board)

__all__ = ["ConnectFourLogic"]
