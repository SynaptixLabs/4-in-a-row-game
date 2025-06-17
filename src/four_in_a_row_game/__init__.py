"""
4-in-a-row-game - A pygame game built with modern Python tooling.

Board game
"""

__version__ = "0.1.0"
__author__ = "Avidor"
__email__ = "avidor@synaptixlabs.ai"

# Import main components for easy access
from .config.game_settings import settings
from .core.constants import GameResult, GameState, PieceType, PlayerType
from .core.exceptions import GameError, GameStateError, InvalidMoveError

__all__ = [
    "settings",
    "GameState",
    "PlayerType",
    "PieceType",
    "GameResult",
    "GameError",
    "InvalidMoveError",
    "GameStateError",
]
