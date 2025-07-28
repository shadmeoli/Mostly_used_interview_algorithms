"""
Implement Conway's Game of Life.

Given an initial state (2D array of 0s and 1s), return the board after N generations.

Rules:
- A cell with 2 or 3 neighbors survives.
- A cell with 3 neighbors becomes alive.
- Otherwise, it dies or stays dead.

Input: board (List[List[int]]), generations (int)
Output: board after given generations
"""

from copy import deepcopy
from python.tester.testLogger import test_runner


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    def count_neighbors(x, y, board):
        rows, cols = len(board), len(board[0])
        return sum(
            board[i][j]
            for i in range(x - 1, x + 2)
            for j in range(y - 1, y + 2)
            if 0 <= i < rows and 0 <= j < cols and (i, j) != (x, y)
        )

    for _ in range(generations):
        rows, cols = len(cells), len(cells[0])
        new_board = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                neighbors = count_neighbors(i, j, cells)
                if cells[i][j] == 1 and neighbors in [2, 3]:
                    new_board[i][j] = 1
                elif cells[i][j] == 0 and neighbors == 3:
                    new_board[i][j] = 1

        cells = new_board

    return cells


@test_runner(
    expected=[
        [
            [0, 1, 0],
            [0, 0, 1],
            [1, 1, 1],
        ],
        [
            [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1]
        ]
    ],
    assert_is_array=True,
    message="Conway's Game of Life Simulation",
)
def test_get_generation(arr):
    cells, generations = arr
    return get_generation(cells, generations)


if __name__ == "__main__":
    test_get_generation([
        ([
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]
        ], 1),
        
    ])