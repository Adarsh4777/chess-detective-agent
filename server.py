from mcp.server.fastmcp import FastMCP
from chess_tools import (
    inspect_position,
    get_legal_moves,
    compare_moves,
    reconstruct_game
)

mcp = FastMCP("Chess Detective")

@mcp.tool()
def inspect_chess_position(fen: str) -> dict:
    """Inspect a chess position, including material, legal moves, and tactical state."""
    return inspect_position(fen)


@mcp.tool()
def investigate_legal_moves(fen: str) -> dict:
    """Investigate all legal moves available in a chess position."""
    return get_legal_moves(fen)


@mcp.tool()
def compare_chess_moves(
    fen: str,
    actual_move: str,
    alternative_move: str
) -> dict:
    """Compare a played move with an alternative move."""
    return compare_moves(fen, actual_move, alternative_move)


@mcp.tool()
def reconstruct_chess_game(pgn_text: str) -> dict:
    """Parse a PGN game and reconstruct every position and move."""
    return reconstruct_game(pgn_text)


if __name__ == "__main__":
    mcp.run()