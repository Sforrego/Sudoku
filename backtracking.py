import random
from classes import Board

def custom_sort(t):
    return t[2]

def backtracking(board, i):

    if len(board.queue) == 0:
        solution = []
        solution.append(i)
        return solution
    #choose the cell with fewest options
    optionsl = {}
    for cell in board.queue:
        options = [k for k in range(1,10) if \
                   (k not in board.info["square"][(cell[0]//3)*3+cell[1]//3] and \
                   k not in board.info["row"][cell[0]] and\
                   k not in board.info["col"][cell[1]])]
        optionsl[cell] = (len(options),cell, options)

    #cell is the empty cell with fewest possible candidates
    cell = sorted(list(optionsl.values()))[0]
    #find the set and value with fewest possible options
    squareslist = []
    for index, square in enumerate(board.info["square"].values()):
        mvalues = [(r,0,[]) for r in range(1,10) if r not in square]
        for index2, value in enumerate(mvalues):
            for row in range(index//3*3, index//3*3+3):
                for col in range(index%3*3, index%3*3+3):
                    if (row, col) in board.queue:
                        if value[0] in optionsl[(row, col)][2]:
                            listoptions = mvalues[index2][2]
                            listoptions.append((row,col))
                            mvalues[index2] = (value[0], mvalues[index2][1]+1,listoptions)

        for value in mvalues:
            if value[1] > 0:
                squareslist.append((index, value[0], value[1], value[2]))
    squareslist.sort(key=custom_sort)
    #squareslist is sorted by the values with fewest options

    rowslist = []
    for index, row in enumerate(board.info["row"].values()):
        mvalues = [(r,0,[]) for r in range(1,10) if r not in row]
        for index2, value in enumerate(mvalues):
            for col in range(9):
                if (index, col) in board.queue:
                    if value[0] in optionsl[(index, col)][2]:
                        listoptions = mvalues[index2][2]
                        listoptions.append((index, col))
                        mvalues[index2] = (value[0], mvalues[index2][1]+1,listoptions)
        for value in mvalues:
            if value[1] > 0:
                rowslist.append((index, value[0], value[1], value[2]))
    rowslist.sort(key=custom_sort)

    colslist = []
    for index, col in enumerate(board.info["col"].values()):
        mvalues = [(r,0,[]) for r in range(1,10) if r not in col]
        for index2, value in enumerate(mvalues):
            for row in range(9):
                if (index, row) in board.queue:
                    if value[0] in optionsl[(index, row)][2]:
                        listoptions = mvalues[index2][2]
                        listoptions.append((row, index))
                        mvalues[index2] = (value[0], mvalues[index2][1]+1,listoptions)
        for value in mvalues:
            if value[1] > 0:
                colslist.append((index, value[0], value[1], value[2]))
    colslist.sort(key=custom_sort)

    real_options = []
    if squareslist:
        a,b,c,d = squareslist[0]
        real_options.append((a,b,c,d))
    if rowslist:
        a,b,c,d = rowslist[0]
        real_options.append((a,b,c,d))
    if colslist:
        a,b,c,d = colslist[0]
        real_options.append((a,b,c,d))
    #options is of the form numer of row/col/square, value (1-9),
    # numbers of and options where te value can go, type of
    if real_options:
        real_options.sort(key=custom_sort)
        best_option = real_options[0]
        if best_option[2] < cell[0] or cell[0] == 0:
            for option in best_option[3]:
                num = best_option[1]
                board.board[option[0]][option[1]] = num
                board.info["square"][(option[0]//3)*3+option[1]//3].append(num)
                board.info["row"][option[0]].append(num)
                board.info["col"][option[1]].append(num)
                board.queue.remove(option)
                solution = backtracking(board, i + 1)
                if solution:
                    solution.append((option[0], option[1], num))
                    return solution
                else:
                    board.board[option[0]][option[1]] = 0
                    board.info["square"][(option[0]//3)*3+option[1]//3].remove(num)
                    board.info["row"][option[0]].remove(num)
                    board.info["col"][option[1]].remove(num)
                    board.queue.append(option)
        else:
            for num in cell[2]:
                board.board[cell[1][0]][cell[1][1]] = num
                board.info["square"][(cell[1][0]//3)*3+cell[1][1]//3].append(num)
                board.info["row"][cell[1][0]].append(num)
                board.info["col"][cell[1][1]].append(num)
                board.queue.remove(cell[1])
                solution = backtracking(board, i + 1)
                if solution:
                    solution.append((cell[1][0], cell[1][1], num))
                    return solution
                else:
                    board.board[cell[1][0]][cell[1][1]] = 0
                    board.info["square"][(cell[1][0]//3)*3+cell[1][1]//3].remove(num)
                    board.info["row"][cell[1][0]].remove(num)
                    board.info["col"][cell[1][1]].remove(num)
                    board.queue.append(cell[1])
    return False
