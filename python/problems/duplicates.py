"""
Write a function that finds duplicates in an
array and returns the duplicatre value.
"""
def findDuplicate(arr: [int]):
    dups = []
    visits = []
    for i in arr:
        if i in visits:
            dups.append(i)
        visits.append(i)
    
    return dups

print(findDuplicate([1,2,3,2,4,3,4]))