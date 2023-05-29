from tree import *
from board import *

tree = Tree()
tree.generate_tree()

board = Board()

print (board)
while True:
    i = int(input("Y:"))
    j = int(input("X:"))
    if board.move(i, j) == None:
        print ("Invalid move\n\n")
        continue
    board = board.move(i, j)
    print (board)
    if board.check_win() == "O":
        print ("You Won!")
        break
    board = tree.tree[board][0]
    print (board)
    if board.check_win() == "X":
        print ("You Lose!")
        break