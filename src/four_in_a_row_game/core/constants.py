"""Game constants for 4-in-a-row-game including colors, dimensions, game states, and configuration values."""

from enum import Enum
from typing import Final

# === Game Dimensions ===
DEFAULT_WINDOW_WIDTH: Final[int] = 800
DEFAULT_WINDOW_HEIGHT: Final[int] = 600
DEFAULT_BOARD_COLS: Final[int] = 7
DEFAULT_BOARD_ROWS: Final[int] = 6
DEFAULT_CONNECT_LENGTH: Final[int] = 4

# === Frame Rate and Timing ===
DEFAULT_FPS: Final[int] = 60
AI_THINK_TIME_MS: Final[int] = 1000
ANIMATION_DURATION_MS: Final[int] = 300
PIECE_DROP_SPEED: Final[float] = 500.0  # Pixels per second


# === Color Constants (RGB) ===
class Colors:
    """Game color constants."""

    # Background and UI
    BACKGROUND: Final[tuple[int, int, int]] = (32, 32, 32)
    BOARD: Final[tuple[int, int, int]] = (64, 128, 255)
    GRID: Final[tuple[int, int, int]] = (128, 128, 128)

    # Player colors
    PLAYER_1: Final[tuple[int, int, int]] = (255, 64, 64)  # Red
    PLAYER_2: Final[tuple[int, int, int]] = (255, 255, 64)  # Yellow

    # UI Elements
    TEXT_PRIMARY: Final[tuple[int, int, int]] = (255, 255, 255)
    TEXT_SECONDARY: Final[tuple[int, int, int]] = (192, 192, 192)
    BUTTON_NORMAL: Final[tuple[int, int, int]] = (96, 96, 96)
    BUTTON_HOVER: Final[tuple[int, int, int]] = (128, 128, 128)
    BUTTON_PRESSED: Final[tuple[int, int, int]] = (64, 64, 64)

    # Game states
    HIGHLIGHT: Final[tuple[int, int, int]] = (255, 255, 255)
    WARNING: Final[tuple[int, int, int]] = (255, 128, 0)
    ERROR: Final[tuple[int, int, int]] = (255, 0, 0)
    SUCCESS: Final[tuple[int, int, int]] = (0, 255, 0)


# === Game State Enums ===
class GameState(str, Enum):
    """Enumeration of possible game states."""

    MENU = "menu"
    PLAYING = "playing"
    PAUSED = "paused"
    GAME_OVER = "game_over"
    SETTINGS = "settings"
    CREDITS = "credits"


class PlayerType(str, Enum):
    """Enumeration of player types."""

    HUMAN = "human"
    AI = "ai"
    REMOTE = "remote"


class PieceType(int, Enum):
    """Enumeration of board piece types."""

    EMPTY = 0
    PLAYER_1 = 1
    PLAYER_2 = 2


class GameResult(str, Enum):
    """Enumeration of game result types."""

    WIN_PLAYER_1 = "win_player_1"
    WIN_PLAYER_2 = "win_player_2"
    DRAW = "draw"
    ONGOING = "ongoing"
    ABORTED = "aborted"


class AILevel(str, Enum):
    """Enumeration of AI difficulty levels."""

    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"
    EXPERT = "expert"


# === Audio Constants ===
class AudioFiles:
    """Audio file path constants."""

    # Sound effects
    PIECE_DROP: Final[str] = "assets/audio/piece_drop.wav"
    PIECE_CONNECT: Final[str] = "assets/audio/piece_connect.wav"
    GAME_WIN: Final[str] = "assets/audio/game_win.wav"
    GAME_DRAW: Final[str] = "assets/audio/game_draw.wav"
    BUTTON_CLICK: Final[str] = "assets/audio/button_click.wav"
    BUTTON_HOVER: Final[str] = "assets/audio/button_hover.wav"

    # Background music
    MENU_MUSIC: Final[str] = "assets/audio/menu_music.ogg"
    GAME_MUSIC: Final[str] = "assets/audio/game_music.ogg"


# === Font Constants ===
class FontSizes:
    """Font size constants."""

    SMALL: Final[int] = 16
    MEDIUM: Final[int] = 24
    LARGE: Final[int] = 36
    XLARGE: Final[int] = 48
    TITLE: Final[int] = 64


# === Layout Constants ===
class Layout:
    """UI layout constants."""

    MARGIN: Final[int] = 20
    PADDING: Final[int] = 10
    BUTTON_WIDTH: Final[int] = 200
    BUTTON_HEIGHT: Final[int] = 50
    BOARD_MARGIN: Final[int] = 50


# === Game Logic Constants ===
DIRECTIONS: Final[list[tuple[int, int]]] = [
    (0, 1),  # Horizontal
    (1, 0),  # Vertical
    (1, 1),  # Diagonal down-right
    (1, -1),  # Diagonal up-right
]

# === Error Messages ===
ERROR_MESSAGES: Final[dict[str, str]] = {
    "invalid_column": "Column {column} is not valid (must be 0-{max_col})",
    "column_full": "Column {column} is full",
    "game_not_active": "Game is not currently active",
    "invalid_player": "Invalid player: {player}",
    "ai_error": "AI player encountered an error: {error}",
    "save_error": "Could not save game: {error}",
    "load_error": "Could not load game: {error}",
}

# === Logging Constants ===
LOG_FORMAT: Final[str] = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
LOG_DATE_FORMAT: Final[str] = "%Y-%m-%d %H:%M:%S"
