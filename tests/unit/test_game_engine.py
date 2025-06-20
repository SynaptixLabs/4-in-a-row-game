"""
Comprehensive test suite for game_engine.py
Designed to achieve 95% contextual coverage for core business logic.
"""

import pygame
import pytest
from unittest.mock import Mock, patch
from four_in_a_row_game.core.game_engine import GameEngine, YourGameLogic
from four_in_a_row_game.config.game_settings import GameSettings


class MockGameLogic:
    """Test implementation of GameLogic protocol."""

    def __init__(self):
        self.update_called = False
        self.input_handled = False
        self.game_over = False

    def update(self, dt: float, game_state) -> None:
        self.update_called = True

    def handle_input(self, events, game_state) -> None:
        self.input_handled = True

    def is_game_over(self, game_state) -> bool:
        return self.game_over


@pytest.fixture
def game_config():
    """Create test game configuration."""
    return GameSettings(
        window_width=800, window_height=600, fps=60, game_title="Test Game"
    )


@pytest.fixture
def mock_pygame():
    """Mock pygame for testing without actual display."""
    with patch("pygame.time.Clock") as mock_clock, patch(
        "pygame.display.flip"
    ) as mock_flip, patch("pygame.event.get") as mock_events:
        mock_clock_instance = Mock()
        mock_clock_instance.tick.return_value = 16.0  # ~60 FPS
        mock_clock.return_value = mock_clock_instance

        mock_events.return_value = []

        yield {"clock": mock_clock_instance, "flip": mock_flip, "events": mock_events}


@pytest.fixture
def game_engine(game_config, mock_pygame):
    """Create test game engine instance."""
    with patch("four_in_a_row_game.core.game_engine.GameState"), patch(
        "four_in_a_row_game.core.game_engine.Renderer"
    ):
        return GameEngine(game_config)


class TestGameEngineInitialization:
    """Test game engine initialization."""

    def test_initialization_sets_config(self, game_engine, game_config):
        """Test that initialization properly sets configuration."""
        assert game_engine.config == game_config
        assert not game_engine.running
        assert game_engine.game_logic is None

    def test_initialization_creates_components(self, game_engine):
        """Test that initialization creates required components."""
        assert game_engine.game_state is not None
        assert game_engine.renderer is not None
        assert game_engine.clock is not None


class TestGameLoop:
    """Test main game loop functionality."""

    def test_run_single_iteration(self, game_engine, mock_pygame):
        """Test single game loop iteration."""
        # Setup: Make game exit after one iteration
        mock_pygame["events"].return_value = [Mock(type=pygame.QUIT)]

        result = game_engine.run()

        assert result == 0  # Success exit code
        assert not game_engine.running
        mock_pygame["clock"].tick.assert_called()
        mock_pygame["flip"].assert_called()

    def test_run_with_game_logic(self, game_engine, mock_pygame):
        """Test game loop with custom game logic."""
        mock_logic = MockGameLogic()
        game_engine.game_logic = mock_logic

        # Exit after one iteration
        mock_pygame["events"].return_value = [Mock(type=pygame.QUIT)]

        game_engine.run()

        assert mock_logic.update_called
        assert mock_logic.input_handled

    def test_run_exception_handling(self, game_engine, mock_pygame):
        """Test game loop exception handling."""
        # Force an exception during update
        with patch.object(game_engine, "update", side_effect=Exception("Test error")):
            result = game_engine.run()

            assert result == 1  # Error exit code


class TestEventHandling:
    """Test event handling functionality."""

    def test_handle_quit_event(self, game_engine):
        """Test handling of quit events."""
        quit_event = Mock(type=pygame.QUIT)
        game_engine.running = True

        game_engine.handle_events([quit_event])

        assert not game_engine.running

    def test_handle_events_with_game_logic(self, game_engine):
        """Test event delegation to game logic."""
        mock_logic = MockGameLogic()
        game_engine.game_logic = mock_logic

        test_events = [Mock(type=123)]  # Non-quit event
        game_engine.handle_events(test_events)

        assert mock_logic.input_handled

    def test_handle_events_without_game_logic(self, game_engine):
        """Test event handling when no game logic is set."""
        # Should not crash when game_logic is None
        game_engine.handle_events([Mock(type=123)])
        # If we get here without exception, test passes


class TestGameUpdate:
    """Test game state update functionality."""

    def test_update_calls_game_state(self, game_engine):
        """Test that update calls game state update."""
        with patch.object(game_engine.game_state, "update") as mock_update:
            game_engine.update(0.016)
            mock_update.assert_called_once_with(0.016)

    def test_update_with_game_logic(self, game_engine):
        """Test update with game logic."""
        mock_logic = MockGameLogic()
        game_engine.game_logic = mock_logic

        game_engine.update(0.016)

        assert mock_logic.update_called

    def test_update_game_over_handling(self, game_engine):
        """Test game over condition handling."""
        mock_logic = MockGameLogic()
        mock_logic.game_over = True
        game_engine.game_logic = mock_logic

        with patch.object(game_engine, "handle_game_over") as mock_game_over:
            game_engine.update(0.016)
            mock_game_over.assert_called_once()


class TestRenderSystem:
    """Test rendering functionality."""

    def test_render_calls_renderer_methods(self, game_engine):
        """Test that render calls appropriate renderer methods."""
        with patch.object(game_engine.renderer, "clear") as mock_clear, patch.object(
            game_engine.renderer, "present"
        ) as mock_present:
            game_engine.render()

            mock_clear.assert_called_once()
            mock_present.assert_called_once()


class TestGameOverHandling:
    """Test game over state management."""

    def test_handle_game_over_logs_message(self, game_engine):
        """Test that game over handler logs appropriate message."""
        with patch("four_in_a_row_game.core.game_engine.logger") as mock_logger:
            game_engine.handle_game_over()
            mock_logger.info.assert_called_with("Game over")


class TestShutdown:
    """Test shutdown functionality."""

    def test_shutdown_stops_running(self, game_engine):
        """Test that shutdown stops the game loop."""
        game_engine.running = True
        game_engine.shutdown()
        assert not game_engine.running

    def test_shutdown_logs_message(self, game_engine):
        """Test that shutdown logs appropriate message."""
        with patch("four_in_a_row_game.core.game_engine.logger") as mock_logger:
            game_engine.shutdown()
            mock_logger.info.assert_called_with("Shutting down game engine")


class TestYourGameLogic:
    """Test the placeholder game logic implementation."""

    def test_your_game_logic_initialization(self):
        """Test YourGameLogic can be instantiated."""
        logic = YourGameLogic()
        assert logic is not None

    def test_your_game_logic_methods(self):
        """Test YourGameLogic implements required methods."""
        logic = YourGameLogic()

        # These should not raise exceptions
        logic.update(0.016, Mock())
        logic.handle_input([], Mock())
        assert logic.is_game_over(Mock()) is False


class TestIntegration:
    """Integration tests for complete game engine functionality."""

    def test_full_game_cycle(self, game_config):
        """Test complete initialization -> run -> shutdown cycle."""
        with patch("four_in_a_row_game.core.game_engine.GameState"), patch(
            "four_in_a_row_game.core.game_engine.Renderer"
        ), patch("pygame.time.Clock") as mock_clock, patch(
            "pygame.display.flip"
        ), patch("pygame.event.get") as mock_events:
            # Setup mocks
            mock_clock_instance = Mock()
            mock_clock_instance.tick.return_value = 16.0
            mock_clock.return_value = mock_clock_instance

            # Make game exit immediately
            mock_events.return_value = [Mock(type=pygame.QUIT)]

            # Test cycle
            engine = GameEngine(game_config)
            result = engine.run()
            engine.shutdown()

            assert result == 0
            assert not engine.running


# Performance and edge case tests
class TestEdgeCases:
    """Test edge cases and error conditions."""

    def test_multiple_quit_events(self, game_engine):
        """Test handling multiple quit events."""
        quit_events = [Mock(type=pygame.QUIT), Mock(type=pygame.QUIT)]
        game_engine.running = True

        game_engine.handle_events(quit_events)

        assert not game_engine.running

    def test_zero_delta_time(self, game_engine):
        """Test update with zero delta time."""
        # Should handle gracefully
        game_engine.update(0.0)

    def test_negative_delta_time(self, game_engine):
        """Test update with negative delta time."""
        # Should handle gracefully (though unrealistic)
        game_engine.update(-0.016)


@pytest.mark.benchmark
class TestPerformance:
    """Performance benchmarks for game engine."""

    def test_update_performance(self, benchmark, game_engine):
        """Benchmark update performance."""
        benchmark(game_engine.update, 0.016)
        # Update should complete quickly

    def test_event_handling_performance(self, benchmark, game_engine):
        """Benchmark event handling performance."""
        events = [Mock(type=i) for i in range(100)]  # 100 random events
        benchmark(game_engine.handle_events, events)
