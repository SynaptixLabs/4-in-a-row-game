"""Core package for 4-in-a-row-game containing constants and exceptions."""

from .constants import (
    DIRECTIONS,
    ERROR_MESSAGES,
    AILevel,
    Colors,
    GameResult,
    GameState,
    PieceType,
    PlayerType,
)
from .exceptions import (
    AIError,
    AudioError,
    BoardError,
    ConfigurationError,
    GameError,
    GameLogicError,
    GameStateError,
    InitializationError,
    InputError,
    InvalidMoveError,
    PlayerError,
    UIError,
)

__all__ = [
    # Constants
    "Colors",
    "GameState",
    "PlayerType",
    "PieceType",
    "GameResult",
    "AILevel",
    "DIRECTIONS",
    "ERROR_MESSAGES",
    # Exceptions
    "GameError",
    "ConfigurationError",
    "InitializationError",
    "GameLogicError",
    "InvalidMoveError",
    "GameStateError",
    "BoardError",
    "PlayerError",
    "AIError",
    "InputError",
    "UIError",
    "AudioError",
]
