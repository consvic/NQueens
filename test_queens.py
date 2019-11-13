import pytest

from queen_util import solveNQueenProblem, foundSolutions, N, transformForDB, changeNQueen, resetGlobal

def test_solutions_8_queens():
    board = [[0 for i in range(N)]
            for j in range(N)]

    solveNQueenProblem(False, board, 0)
    solutions = foundSolutions()
    resetGlobal()
    assert solutions == 92, "Should be 92"

def test_solutions_4_queens():
    changeNQueen(4)
    board = [[0 for i in range(4)]
            for j in range(4)]
    solveNQueenProblem(False, board, 0)
    solutions = foundSolutions()
    resetGlobal()
    assert solutions == 2, "Should be 2"

def test_solutions_7_queens():
    changeNQueen(7)
    board = [[0 for i in range(7)]
            for j in range(7)]

    solveNQueenProblem(False, board, 0)
    solutions = foundSolutions()
    resetGlobal()
    assert solutions == 40, "Should be 40"

def test_solutions_9_queens():
    changeNQueen(9)
    board = [[0 for i in range(9)]
            for j in range(9)]

    solveNQueenProblem(False, board, 0)
    solutions = foundSolutions()
    resetGlobal()
    assert solutions == 352, "Should be 352"

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
