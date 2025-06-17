"""Configuration package for 4-in-a-row-game."""

from .game_settings import GameSettings, load_game_settings, settings

__all__ = ["settings", "GameSettings", "load_game_settings"]
