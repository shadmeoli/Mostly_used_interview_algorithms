"""
Given two different positions on a chess board,
find the least number of moves it would take a knight
to get from one to the other. The positions will be
passed as two arguments in algebraic notation.

For example, knight("a3", "b5") should return 1.

The knight is not allowed to move off the board.
The board is 8x8.
"""


def Board():
    cells = ["a", "b", "c", "d", "e", "f", "g", "h"]
    board = []
    for i in range(0, 8):
        row = []
        for cell in cells:
            row.append(f"{cell}{i+1}")
        board.append(row)
    return board


def valid_moves(pos):
    moves = []
    col, row = ord(pos[0]) - ord("a"), int(pos[1]) - 1
    for dr, dc in [
        (2, 1),
        (1, 2),
        (-1, 2),
        (-2, 1),
        (-2, -1),
        (-1, -2),
        (1, -2),
        (2, -1),
    ]:
        new_row, new_col = row + dr, col + dc
        if 0 <= new_row < 8 and 0 <= new_col < 8:
            moves.append(chr(new_col + ord("a")) + str(new_row + 1))
    return moves


def knight(p1: str, p2: str):
    board = Board()
    queue = [(p1, 0)]
    visited = set()
    visited.add(p1)

    while queue:
        pos, distance = queue.pop(0)
        if pos == p2:
            return distance
        for move in valid_moves(pos):
            if move not in visited:
                queue.append((move, distance + 1))
                visited.add(move)
    return -1


print(knight("a3", "b4"))