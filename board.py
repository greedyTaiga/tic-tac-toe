from sequence import *

EMPTY_CHAR = '_'

class Board:
    turns = {
        'X':'O',
        'O':'X'
    }
    def __init__(self, size = 3, turn = "O", board = None):
        if board == None:
            board = []
            for i in range(size):
                row = [EMPTY_CHAR] * size
                board.append(row)
        self.board = board
        self.size = size
        self.turn = turn

    def next_turn(self):
       return Board.turns[self.turn]

    def all_possible_moves(self):
        moves = []
        for i in range(self.size):
            for j in range(self.size):
                m = self.move(i, j)
                if m != None:
                    moves.append(m)
        return moves

    def move(self, i, j):
        if i < 0 or i >= self.size:
            return None
        if j < 0 or j >= self.size:
            return None
        
        if self.board[i][j] != EMPTY_CHAR:
            return None

        new_board = Board(self.size, self.next_turn(), self.copy_board())
        new_board.board[i][j] = self.turn

        return new_board

    def check_win(self):
        if self.check_win_with_turn("O"):
            return "O"
        if self.check_win_with_turn("X"):
            return "X"
        if len(self.all_possible_moves()) == 0:
            return "D"
        return "-"

    def check_win_with_turn(self, turn):
        res = False
        win_seq = [turn] * min(4, self.size)
        
        res = res or check_sub_in_matrix(self.board, win_seq)
        res = res or check_sub_in_matrix(turn90(self.board), win_seq)
        res = res or check_sub_in_diag(self.board, win_seq)
        res = res or check_sub_in_diag(mirror_y(self.board), win_seq)

        return res

    def copy_board(self):
        new_board = []
        for row in self.board:
            new_board.append(row.copy())
        return new_board

    def __repr__(self):
        res = ""
        for i in self.board:
            res += '|'.join(i) + "\n"
        return res
    
    def __eq__(self, othr):
        return (isinstance(othr, type(self))
                and (self.board, self.turn, self.size) ==
                    (othr.board, othr.turn, othr.size))

    def __hash__(self):
        return hash((self.__repr__(), self.turn, self.size))