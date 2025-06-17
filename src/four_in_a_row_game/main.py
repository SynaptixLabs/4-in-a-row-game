#!/usr/bin/env python3
"""
4-in-a-row-game - Main Entry Point

A Python pygame game built with modern development practices.

TODO: Implement your specific game logic based on your requirements.
"""

import logging
import sys

try:
    import pygame
except ImportError:
    print("pygame is not installed. Install it with: poetry add pygame")
    sys.exit(1)

from four_in_a_row_game.core.config import GameConfig
from four_in_a_row_game.core.game_engine import GameEngine
from four_in_a_row_game.utils.logging_setup import setup_logging


def main() -> int:
    """
    Main entry point for 4-in-a-row-game.

    Returns:
        Exit code: 0 for success, non-zero for error
    """
    try:
        # Setup logging
        setup_logging()
        logger = logging.getLogger(__name__)
        logger.info("Starting 4-in-a-row-game")

        # Load configuration
        config = GameConfig()

        # Initialize pygame
        pygame.init()
        logger.info("Pygame initialized successfully")

        # Create and run game engine
        engine = GameEngine(config)
        result = engine.run()

        logger.info("Game finished successfully")
        return result

    except KeyboardInterrupt:
        print("\n4-in-a-row-game interrupted by user")
        return 0
    except Exception as e:
        logger = logging.getLogger(__name__)
        logger.error(f"Game error: {e}", exc_info=True)
        print(f"Error running 4-in-a-row-game: {e}")
        return 1
    finally:
        # Cleanup pygame
        pygame.quit()


if __name__ == "__main__":
    sys.exit(main())
