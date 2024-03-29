import sys
import csv
from classes import Board
from backtracking import backtracking

#https://dlbeer.co.nz/articles/sudoku.html
def board_loader(board):
    with open(board) as f:
        board = csv.reader(f)
        board = [i for i in board]
    return board


if __name__ == "__main__":
    board = sys.argv[1]

    board = board_loader(board)

    board = Board(board)

    sol = backtracking(board, 0)

    if sol:
        total = sol[0]
        moves = sol[1:]

        for i in moves:
            board.board[i[0]][i[1]] = i[2]
        print("success")
    else:
        print("fail")
