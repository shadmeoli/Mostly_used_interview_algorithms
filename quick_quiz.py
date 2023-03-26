'''
            [ QUESTION ]
Build a pyramid-shaped tower, as an array/list of strings,
given a positive integer number of floors.
A tower block is represented with "*" character.

result = ['  *  ', ' *** ', '*****']

'''

def tower_builder(n_floors):
    tower = []
    for i in range(n_floors):
        blocks = '*' * (2 * i + 1)
        spaces = ' ' * (n_floors - i - 1)
        tower.append(spaces + blocks + spaces)

    max_floor_length = len(tower[-1])
    for i in range(len(tower)):
        spaces_to_add = (max_floor_length - len(tower[i])) // 2
        tower[i] = " "*spaces_to_add + tower[i]

    return tower



if __name__ == "__main__":
    print(tower_builder(3))