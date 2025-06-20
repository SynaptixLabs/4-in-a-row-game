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

    def present(self) -> None:
        """Present the current frame (handled by game engine with pygame.display.flip)."""
        # This is called by the game engine, but we don't call flip here
        # to avoid double-flipping. The game engine calls pygame.display.flip()
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
