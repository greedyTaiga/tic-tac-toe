from board import *

class Tree:
    
    def __init__(self):
        self.tree = {}
        self.start_board = Board()
    
    def generate_tree(self):
        self.travel(self.start_board)

    def travel(self, cur_board):

        if cur_board in self.tree:
            return self.tree[cur_board][1]

        res = cur_board.check_win()
        if res == 'O':
            return 10
        elif res == 'X':
            return -10
        elif res == 'D':
            return 0
        
        max_board, min_board = None, None
        max_val, min_val = 0, 0

        for next_board in cur_board.all_possible_moves():
            val = self.travel(next_board)
            if min_board == None or val < min_val:
                min_board = next_board
                min_val = val
            if max_board == None or val > max_val:
                max_board = next_board
                max_val = val
        
        if cur_board.turn == 'O':
            self.tree[cur_board] = (max_board, max_val)
            return max_val
        else:
            self.tree[cur_board] = (min_board, min_val)
            return min_val

        
