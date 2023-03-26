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


# this is a move compact version of the above function
def tower_builder2(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

if __name__ == "__main__":
    import time

    start = time.time()
    print(tower_builder(5))
    print(f'Tower function 1 ran for {time.time()-start} sec')


    start2 = time.time()
    print(tower_builder2(5))
    print(f'Tower function 2 ran for {time.time()-start2} sec')
