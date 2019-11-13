import pytest

from queen_util import solveNQueenProblem, foundSolutions, N, transformForDB

def test_solutions_8_queens():
    board = [[0 for i in range(N)]
            for j in range(N)]

    solveNQueenProblem(False, board, 0)
    solutions = foundSolutions()

    assert solutions == 92, "Should be 92"

def test_transform():
    resultBoard = [[0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
            [1, 0, 0, 0, 0, 0, 0, 0]]

    simpleBoardFormat = transformForDB(resultBoard)
    
    assert simpleBoardFormat[0] == 2, 'Should be 2'
    assert simpleBoardFormat[1] == 5, 'Should be 5'
    assert simpleBoardFormat[4] == 7, 'Should be 7'
    assert simpleBoardFormat[6] == 6, 'Should be 6'



     