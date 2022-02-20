"""The given class adds an incremental transposition table to the existing Board class
which gets updated on every push or pop. The transposition table is a dictionary mapping
which takes a board representation as key and returns the number of
repetitions for this board in the current board stack (game)."""

from chess import *
import chess.pgn as pgn

class Board(Board):

    def __init__(self, fen: Optional[str] = STARTING_FEN, *, chess960: bool = False) -> None:
        super().__init__(fen, chess960=chess960)
        self._transposition_table: Dict[Hashable, int] = {self._transposition_key(): 0}

    def set_fen(self, fen: str) -> None:
        super().set_fen(fen)
        self._transposition_table = {self._transposition_key(): 0}

    def push(self, move: Move) -> None:
        super().push(move)
        key = self._transposition_key()
        if key in self._transposition_table:
            self._transposition_table[key] += 1
        else:
            self._transposition_table[key] = 0

    def pop(self) -> Move:
        key = self._transposition_key()
        if self._transposition_table[key] == 0:
            del self._transposition_table[key]
        else:
            self._transposition_table[key] -= 1
        return super().pop()

    def is_repetition(self, count: int = 3) -> bool:
        return self._transposition_table[self._transposition_key()] >= count


if __name__ == "__main__":
    board = Board()
    print(board._transposition_table)
    print(board.fen())
    board.push(list(board.legal_moves)[0])
    print(board._transposition_table)
    print(board.fen())
    print(board.pop())
    print(board._transposition_table)
    print(board.fen())