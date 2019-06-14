class Board():
    def __init__(self, board):
        self.board =[[0 for i in range(9)] for j in range(9)]
        self.info = {}
        self.info["square"] = {i:[] for i in range(9)}
        self.info["row"] = {i:[] for i in range(9)}
        self.info["col"] = {i:[] for i in range(9)}
        self.queue = []
        for row,_ in enumerate(board):
            for col,_ in enumerate(board):
                if board[row][col] == "0":
                    board[row][col] = 0
                    self.queue.append((row,col))
                else:
                     self.info["square"][(row//3)*3+col//3].append(int(board[row][col]))
                     self.info["row"][row].append(int(board[row][col]))
                     self.info["col"][col].append(int(board[row][col]))
                     self.board[row][col] = int(board[row][col])
        self.checked = {x:0 for x in self.queue}
    def __str__(self):
        string = "-----SUDOKU------\n"
        for i in self.board:
            i = [str(k) if k>0 else " " for k in i ]
            string += " ".join(i)
            string += "\n"
        return string
