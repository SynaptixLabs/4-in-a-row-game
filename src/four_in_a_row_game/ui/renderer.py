"""Rendering system for the game using pygame."""

import pygame
from typing import Optional
from four_in_a_row_game.config.game_settings import GameSettings


class Renderer:
    """
    Handles all rendering operations for the game.

    Manages:
    - Screen initialization and management
    - Drawing operations and coordination
    - Frame presentation
    """

    def __init__(self, config: GameSettings):
        """
        Initialize the renderer with game configuration.

        Args:
            config: Game settings containing display configuration
        """
        self.config = config
        self.screen: Optional[pygame.Surface] = None
        self._initialize_display()

    def _initialize_display(self) -> None:
        """Initialize pygame display."""
        pygame.init()
        self.screen = pygame.display.set_mode(self.config.window_size)
        pygame.display.set_caption(self.config.game_title)

    def clear(self) -> None:
        """Clear the screen with the background color."""
        if self.screen:
            self.screen.fill(self.config.background_color)

    # ---------------------- Drawing helpers ----------------------
    def draw_board(
        self,
        board_state,
        hover_col: int | None = None,
    ) -> None:
        """Render the board grid, pieces, and hover preview.

        Args:
            board_state: BoardState instance holding current grid.
            hover_col: Column index currently under the mouse or None.
        """
        if not self.screen:
            return

        rows = len(board_state.grid)
        cols = len(board_state.grid[0]) if rows else 0
        screen_w, screen_h = self.config.window_size

        # Determine cell size to fit board nicely with margin
        margin = 20
        cell_size = min(
            (screen_w - 2 * margin) // cols,
            (screen_h - 2 * margin) // rows,
        )
        board_w = cell_size * cols
        board_h = cell_size * rows
        board_x = (screen_w - board_w) // 2
        board_y = (screen_h - board_h) // 2

        # Draw board background
        import pygame  # local import to avoid circular
        from four_in_a_row_game.core.constants import Colors, PieceType

        pygame.draw.rect(
            self.screen,
            Colors.BOARD,
            pygame.Rect(board_x, board_y, board_w, board_h),
            border_radius=4,
        )

        # Draw cells (holes and pieces)
        radius = cell_size // 2 - 4
        for r in range(rows):
            for c in range(cols):
                cx = board_x + c * cell_size + cell_size // 2
                cy = board_y + r * cell_size + cell_size // 2
                piece = board_state.grid[r][c]
                color = Colors.BACKGROUND  # empty hole background
                if piece == PieceType.PLAYER_1:
                    color = Colors.PLAYER_1
                elif piece == PieceType.PLAYER_2:
                    color = Colors.PLAYER_2
                pygame.draw.circle(self.screen, color, (cx, cy), radius)

        # Draw hover preview disc at top row if column available
        if hover_col is not None and 0 <= hover_col < cols:
            # Find first empty row from bottom
            target_row = None
            for r in range(rows - 1, -1, -1):
                if board_state.grid[r][hover_col] == PieceType.EMPTY:
                    target_row = r
                    break
            if target_row is not None:
                cx = board_x + hover_col * cell_size + cell_size // 2
                cy = board_y + target_row * cell_size + cell_size // 2
                # Semi-transparent white outline
                preview_surf = pygame.Surface((radius*2, radius*2), pygame.SRCALPHA)
                pygame.draw.circle(preview_surf, (*Colors.HIGHLIGHT, 120), (radius, radius), radius)
                self.screen.blit(preview_surf, (cx - radius, cy - radius))

    def present(self) -> None:
        """Present the current frame (handled by game engine with pygame.display.flip)."""
        # GameEngine flips the display; nothing to do here
        pass

    def get_screen(self) -> Optional[pygame.Surface]:
        """
        Get the pygame screen surface.

        Returns:
            The pygame screen surface, or None if not initialized
        """
        return self.screen

    def shutdown(self) -> None:
        """Clean shutdown of the renderer."""
        pygame.quit()
