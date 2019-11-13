''' N-Queen problem with recursion (backtracking) '''
# Reference code https://www.geeksforgeeks.org/printing-solutions-n-queen-problem/
N = 8
k = 1

solutions = []

''' This function is to print a board with the places queens '''
def printBoard(board):
    global k
    print(k, ")\n")
    for row in range(N):
        for column in range(N):
            print(board[row][column], end = " ")
        print("\n")
    print("\n")

''' This function returns the number of solutions found,
need to run solveNQueenProblem first to proper show the result'''
def foundSolutions():
    global k
    return k - 1

''' This function prepares the data for the DB'''
def transformForDB(board):
    simpleBoardFormat = []
    for row in range(N):
        for column in range(N):
            if board[row][column] == 1:
                simpleBoardFormat.append(column)

    return simpleBoardFormat

''' This function is to check if a queen can be added to our board
in a particular row and column (since we are placing queens from left to right
we only need to check the diagonals on the left side)'''
def isValidSpot(board, row, column):
    isValid = True

    ''' Check the row '''
    for index in range(column):
        if (board[row][index]):
            isValid = False
            return isValid

    ''' Check upper diagonal '''
    rowPosition = row
    columnPosition = column

    while rowPosition >= 0 and columnPosition >= 0:
        if board[rowPosition][columnPosition]:
            isValid = False
            return isValid
        rowPosition -= 1
        columnPosition -= 1

    ''' Check lower diagonal '''
    rowPosition = row
    columnPosition = column

    while rowPosition < N and columnPosition >= 0:
        if board[rowPosition][columnPosition]:
            isValid = False
            return isValid
        rowPosition += 1
        columnPosition -= 1

    return isValid

''' This function does all the magic, gives you the option to print the board results
and starts the backtracking, you need and empty board and column 0 to start '''
def solveNQueenProblem(printRes, board, column):
    res = False

    ''' Break recursion if we found a solution we print result and transform the data'''
    if column == N:
        simpleBoardFormat = transformForDB(board)
        solutions.append(simpleBoardFormat)
        if printRes:
            printBoard(board)
        global k
        k = k + 1
        res = True
        return res

    for index in range(N):
        if isValidSpot(board, index, column):
            ''' 1 is our Queen '''
            board[index][column] = 1

            res = solveNQueenProblem(printRes, board, column + 1) or res

            ''' Backtrack in case we don't find a solution '''
            board[index][column] = 0
    
    return res

''' This test is mostly for tests, to try out new Ns,
careful how you use it, might screw up the Ns'''
def changeNQueen(newN):
    global N
    N = newN

''' This function resets the global values '''
def resetGlobal():
    global N, k
    N = 8
    k = 1