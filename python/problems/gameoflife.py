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

from preloaded import htmlize  # this can help you debug your code


def get_generation(cells: list[list[int]], generations: int) -> list[list[int]]:
    rows = len(cells)
    cols = len(cells[0])

    for cycle in range(generations):
        new_cells = [[0] * cols for _ in range(rows)]

        for row in range(rows):
            for col in range(cols):
                neighbors = (
                    sum(
                        cells[i][j]
                        for i in range(row - 1, row + 2)
                        for j in range(col - 1, col + 2)
                        if 0 <= i < rows and 0 <= j < cols
                    )
                    - cells[row][col]
                )
                if cells[row][col] == 1 and 2 <= neighbors <= 3:
                    new_cells[row][col] = 1
                elif cells[row][col] == 0 and neighbors == 3:
                    new_cells[row][col] = 1

        cells = new_cells
        print(htmlize(cells))

    return cells


if __name__ == "__main__":
    cells = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 2, 1, 1, 1, 1, 0, 0],
        [0, 0, 2, 1, 1, 1, 1, 0, 0],
        [0, 3, 2, 1, 1, 1, 1, 0, 0],
    ]

    print(get_generation(cells, 3))

