''' N-Queen problem with recursion (backtracking) '''
N = 8
k = 1

''' This function is to print a board with the places queens '''
def printBoard(board):
    global k
    print(k, ")\n")
    k = k + 1
    for row in range(N):
        for column in range(N):
            print(board[row][column], end = " ")
        print("\n")
    print("\n")

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
        if (board[rowPosition][columnPosition]):
            isValid = False
            return isValid
        rowPosition -= 1
        columnPosition -= 1

    ''' Check lower diagonal '''
    rowPosition = row
    columnPosition = column

    while rowPosition < N and columnPosition >= 0:
        if (board[rowPosition][columnPosition]):
            isValid = False
            return isValid
        rowPosition += 1
        columnPosition -= 1

    return isValid

def solveNQueenProblem(board, column):
    res = False

    ''' Break recursion if we found a solution '''
    if (column == N):
        printBoard(board)
        res = True
        return res

    for index in range(N):
        if (isValidSpot(board, index, column)):
            ''' 1 is our Queen '''
            board[index][column] = 1

            res = solveNQueenProblem(board, column + 1) or res

            ''' Backtrack in case we don't find a solution '''
            board[index][column] = 0
    
    return res

def main():
    board = [[0 for i in range(N)]
                for j in range(N)]

    if (solveNQueenProblem(board, 0) == False):
        print("Sorry we could not find a solution")

main()
