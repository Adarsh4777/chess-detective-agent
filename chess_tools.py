import chess
import chess.pgn
import io


def inspect_position(fen: str):
    board = chess.Board(fen)

    pieces = {
        "white": {
            "pawns": len(board.pieces(chess.PAWN, chess.WHITE)),
            "knights": len(board.pieces(chess.KNIGHT, chess.WHITE)),
            "bishops": len(board.pieces(chess.BISHOP, chess.WHITE)),
            "rooks": len(board.pieces(chess.ROOK, chess.WHITE)),
            "queens": len(board.pieces(chess.QUEEN, chess.WHITE)),
        },
        "black": {
            "pawns": len(board.pieces(chess.PAWN, chess.BLACK)),
            "knights": len(board.pieces(chess.KNIGHT, chess.BLACK)),
            "bishops": len(board.pieces(chess.BISHOP, chess.BLACK)),
            "rooks": len(board.pieces(chess.ROOK, chess.BLACK)),
            "queens": len(board.pieces(chess.QUEEN, chess.BLACK)),
        }
    }

    legal_moves = [board.san(move) for move in board.legal_moves]

    return {
        "fen": fen,
        "turn": "White" if board.turn else "Black",
        "is_check": board.is_check(),
        "is_checkmate": board.is_checkmate(),
        "material": pieces,
        "legal_move_count": len(legal_moves),
        "sample_legal_moves": legal_moves[:15]
    }


def get_legal_moves(fen: str):
    board = chess.Board(fen)

    moves = []
    for move in board.legal_moves:
        moves.append({
            "san": board.san(move),
            "uci": move.uci(),
            "capture": board.is_capture(move),
            "check": board.gives_check(move)
        })

    return {
        "turn": "White" if board.turn else "Black",
        "moves": moves
    }


def compare_moves(fen: str, actual_move: str, alternative_move: str):
    board = chess.Board(fen)

    try:
        actual = board.parse_san(actual_move)
        actual_is_capture = board.is_capture(actual)
        actual_is_check = board.gives_check(actual)

        board.parse_san(alternative_move)

        return {
            "actual_move": actual_move,
            "alternative_move": alternative_move,
            "actual_is_capture": actual_is_capture,
            "actual_is_check": actual_is_check,
            "message": f"The played move {actual_move} was compared with the alternative {alternative_move}."
        }

    except Exception as e:
        return {"error": str(e)}


def reconstruct_game(pgn_text: str):
    game = chess.pgn.read_game(io.StringIO(pgn_text))

    if game is None:
        return {"error": "Could not parse PGN."}

    board = game.board()
    moves = []

    for move_number, move in enumerate(game.mainline_moves(), start=1):
        san = board.san(move)
        fen_before = board.fen()

        moves.append({
            "ply": move_number,
            "move": san,
            "fen_before": fen_before
        })

        board.push(move)

    return {
        "headers": dict(game.headers),
        "result": game.headers.get("Result", "*"),
        "total_plies": len(moves),
        "moves": moves
    }