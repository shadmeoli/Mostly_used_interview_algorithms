'''
            [ QUESTION ]
Build a pyramid-shaped tower, as an array/list of strings,
given a positive integer number of floors.
A tower block is represented with "*" character.

result = ['  *  ', ' *** ', '*****']

'''
# this is a move compact version of the above function
def tower_builder2(n):
    return [("*" * (i*2-1)).center(n*2-1) for i in range(1, n+1)]

def lcm(nums)-> int:
    iters = []
    if iters:
        while max(iters) > 1: 
            for i in range(0, len(nums)):
                iters.append(nums[i]//max(iters))
    else:
        for i in range(0, len(nums)):
            iters.append(nums[i]//2)
    return iters
