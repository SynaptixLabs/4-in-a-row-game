"""
Game Engine - Core Infrastructure

This module provides the foundational game engine infrastructure.
Implement your specific game logic by extending or modifying this base.

TODO: Define your specific game requirements and implement them here.
"""

import logging
from typing import Protocol

import pygame

from four_in_a_row_game.config.game_settings import GameSettings
from four_in_a_row_game.game.game_state import GameState
from four_in_a_row_game.ui.renderer import Renderer

logger = logging.getLogger(__name__)


class GameLogic(Protocol):
    """Protocol defining the interface for game-specific logic."""

    def update(self, dt: float, game_state: GameState) -> None:
        """Update game logic for one frame."""
        ...

    def handle_input(
        self, events: list[pygame.event.Event], game_state: GameState
    ) -> None:
        """Handle input events."""
        ...

    def is_game_over(self, game_state: GameState) -> bool:
        """Check if the game is over."""
        ...


class GameEngine:
    """
    Core game engine handling the main game loop.

    This provides the infrastructure for:
    - Game loop management
    - Frame rate control
    - Input handling coordination
    - Rendering coordination
    - State management

    Extend or modify this class to implement your specific game.
    """

    def __init__(self, config: GameSettings) -> None:
        """Initialize the game engine."""
        self.config = config
        self.running = False
        self.clock = pygame.time.Clock()
        # Initialize core components
        self.game_state = GameState()
        self.renderer = Renderer(config)

        # Initialize Connect-Four-specific logic
        from four_in_a_row_game.game.connect_four_logic import ConnectFourLogic

        self.game_logic = ConnectFourLogic(config)
        logger.info("Game engine initialized")

    def run(self) -> int:
        """
        Main game loop.

        Returns:
            Exit code: 0 for success, non-zero for error
        """
        logger.info("Starting game loop")
        self.running = True

        try:
            while self.running:
                # Calculate delta time
                dt = self.clock.tick(self.config.fps) / 1000.0

                # Handle events
                events = pygame.event.get()
                self.handle_events(events)

                # Update game state
                self.update(dt)

                # Render frame
                self.render()

                # Update display
                pygame.display.flip()

        except Exception as e:
            logger.error(f"Game loop error: {e}")
            return 1

        logger.info("Game loop finished")
        return 0

    def handle_events(self, events: list[pygame.event.Event]) -> None:
        """Handle input events."""
        for event in events:
            if event.type == pygame.QUIT:
                self.running = False
            # TODO: Add your specific event handling here
        # Delegate to game-specific logic
        if self.game_logic:
            self.game_logic.handle_input(events, self.game_state)

    def update(self, dt: float) -> None:
        """Update game state for one frame."""
        # Update core systems
        self.game_state.update(dt)

        # --- Input hover column tracking ---
        mouse_x, _ = pygame.mouse.get_pos()
        self._hover_col = None
        if self.renderer.screen:
            board_w = self.config.window_size[0]
            cols = self.config.board_width
            cell_size = (board_w - 40) // cols  # assumes margin 20 like renderer
            board_x = (self.config.window_size[0] - (cell_size * cols)) // 2
            rel_x = mouse_x - board_x
            if 0 <= rel_x < cell_size * cols:
                self._hover_col = rel_x // cell_size

        # Update logic
        self.game_logic.update(dt, self.game_state)


        # Check for game over conditions
        if self.game_logic.is_game_over(self.game_state):
            self.handle_game_over()

    def render(self) -> None:
        """Render the current frame."""
        self.renderer.clear()
        if hasattr(self.renderer, "draw_board"):
            self.renderer.draw_board(self.game_logic.board, getattr(self, "_hover_col", None))
        # Future: draw turn indicator here
        self.renderer.present()

    def handle_game_over(self) -> None:
        """Handle game over state."""
        logger.info("Game over")
        # TODO: Implement game over logic
        # - Show game over screen
        # - Save scores
        # - Offer restart option
        # - etc.

    def shutdown(self) -> None:
        """Clean shutdown of the game engine."""
        logger.info("Shutting down game engine")
        self.running = False

        # TODO: Add any cleanup code here
        # - Save game state
        # - Release resources
        # - etc.


# TODO: Implement your specific game logic class
class YourGameLogic:
    """
    Implement your specific game logic here.

    This should implement the GameLogic protocol above.
    """

    def update(self, dt: float, game_state: GameState) -> None:
        """Update your game logic."""
        # TODO: Implement your game's update logic

    def handle_input(
        self, events: list[pygame.event.Event], game_state: GameState
    ) -> None:
        """Handle your game's input."""
        # TODO: Implement your game's input handling

    def is_game_over(self, game_state: GameState) -> bool:
        """Check if your game is over."""
        # TODO: Implement your game over conditions
        return False
