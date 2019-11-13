import sqlalchemy
from sqlalchemy.sql import select
from sqlalchemy import Column, Integer, ARRAY

connection_string = 'postgresql://user:pass@postgresql/mydatabase'

db = sqlalchemy.create_engine(connection_string)  
engine = db.connect() 
meta = sqlalchemy.MetaData(engine)
meta.reflect(bind=engine)

''' N-Queen problem with recursion (backtracking) '''
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

''' This functions stores the data in the DB only if there are solutions'''
def storeDataInDB():
    if len(solutions) > 0:
        record = sqlalchemy.table("queensolutions",
                                    Column("solution_index", Integer),
                                    Column("number_queens", Integer),
                                    Column("solution", ARRAY(Integer)))

        for num, solution in enumerate(solutions, start=1):
            statement = record.insert().values(
                solution_index = num,
                number_queens = N,
                solution = solution,
            )
            engine.execute(statement)

''' This function ugly prints all the table entries '''
def printTable():
    table = meta.tables["queensolutions"]
    resultSelect = engine.execute(select([table.c.solution_index, table.c.number_queens, table.c.solution]))
    rows = resultSelect.fetchall()
    print(rows)

''' This function fetches for entries for current N'''
def fetchForNQueenTableEntries():
    table = meta.tables["queensolutions"]
    resultSelectNQueen = engine.execute(select([table.c.number_queens]).where(table.c.number_queens == N))
    rows = resultSelectNQueen.fetchall()

    return rows

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

def main():
    board = [[0 for i in range(N)]
                for j in range(N)]

    if solveNQueenProblem(True, board, 0) == False:
        print("Sorry we could not find a solution")
        return

    entries = fetchForNQueenTableEntries()

    if len(entries) > 0:
        print(f"No need to store we already have solutions for {N} Queen")
        return
    
    storeDataInDB()
    printTable()

main()
