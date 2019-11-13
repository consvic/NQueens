import sqlalchemy
from sqlalchemy.sql import select
from sqlalchemy import Column, Integer, ARRAY

from queen_util import *

connection_string = 'postgresql://user:pass@postgresql/mydatabase'

db = sqlalchemy.create_engine(connection_string)  
engine = db.connect() 
meta = sqlalchemy.MetaData(engine)
meta.reflect(bind=engine)

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
