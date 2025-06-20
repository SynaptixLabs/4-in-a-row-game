"""Unit tests for BoardState logic."""
from four_in_a_row_game.game.board import BoardState
from four_in_a_row_game.core.constants import GameResult, PieceType
from four_in_a_row_game.core.exceptions import InvalidMoveError


def test_drop_piece_alternates_players() -> None:
    board = BoardState.new(rows=6, cols=7)
    board2 = board.drop_piece(0)
    board3 = board2.drop_piece(0)
    assert board2.grid[5][0] == PieceType.PLAYER_1
    assert board3.grid[4][0] == PieceType.PLAYER_2


def test_invalid_column_raises() -> None:
    board = BoardState.new()
    try:
        board.drop_piece(999)
    except InvalidMoveError:
        pass
    else:
        assert False, "Expected InvalidMoveError"


def test_column_full_raises() -> None:
    board = BoardState.new(rows=2, cols=1)
    board = board.drop_piece(0)
    board = board.drop_piece(0)
    try:
        board.drop_piece(0)
    except InvalidMoveError:
        pass
    else:
        assert False, "Expected InvalidMoveError when column full"


def test_horizontal_win() -> None:
    """Player 1 should win horizontally in the bottom row."""
    board = BoardState.new(rows=2, cols=4)
    # Build sequence so Player 1 occupies bottom row columns 0-3
    moves = [0, 0, 1, 1, 2, 2, 3]  # P1, P2 alternating
    for col in moves:
        board = board.drop_piece(col)
    assert board.winner() == GameResult.WIN_PLAYER_1


def test_draw_detection() -> None:
    board = BoardState.new(rows=1, cols=1)
    board = board.drop_piece(0)
    assert board.winner() == GameResult.DRAW


def test_vertical_win() -> None:
    """Player 1 should win vertically in column 0."""
    board = BoardState.new(rows=4, cols=2)
    moves = [0, 1, 0, 1, 0, 1, 0]  # P1 drops in col0, P2 in col1
    for col in moves:
        board = board.drop_piece(col)
    assert board.winner() == GameResult.WIN_PLAYER_1


def test_board_str() -> None:
    """Calling str() on board should yield ascii grid without error."""
    board = BoardState.new(rows=2, cols=2)
    board = board.drop_piece(0)
    s = str(board)
    assert "X" in s
