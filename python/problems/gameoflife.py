import os
os.system("pip install codewars_test")

import codewars_test as test
from solution import get_generation
from preloaded import htmlize
from copy import deepcopy


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    rows = len(cells)
    cols = len(cells[0])

    for cycle in range(generations):
        new_cells = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                neighbors = sum(cells[i][j] for i in range(row-1, row+2) for j in range(col-1, col+2)
                                if 0 <= i < rows and 0 <= j < cols) - cells[row][col]
                if cells[row][col] == 1 and 2 <= neighbors <= 3:
                    new_cells[row][col] = 1
                elif cells[row][col] == 0 and neighbors == 3:
                    new_cells[row][col] = 1

        cells = new_cells

    return cells



@test.describe('tests')
def tests():

    def do_test(input, generations, expected):
        actual = get_generation(deepcopy(input), generations)
        message =\
            f'for cells:\n{htmlize(input)}\nafter {generations} generations,' +\
            f' expected:\n{htmlize(expected)}\nbut got:\n{htmlize(actual)}'
        test.assert_equals(actual, expected, message)

    @test.it('One glider')
    def one_glider():
        do_test([
            [1,0,0],
            [0,1,1],
            [1,1,0]
        ], 1, [
            [0,1,0],
            [0,0,1],
            [1,1,1]
        ])

    @test.it('Two gliders')
    def two_gliders():
        do_test([
            [1,1,1,0,0,0,1,0],
            [1,0,0,0,0,0,0,1],
            [0,1,0,0,0,1,1,1]
        ], 16, [
            [1,1,1,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1]
        ])



