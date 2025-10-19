"""
Write a function that finds duplicates in an
array and returns the duplicatre value.
"""


def findDuplicate(arr: list[int]):
    # dups = []
    # for idx, i in enumerate(arr):
    #     if i in arr[:idx]:
    #         dups.append(i)
    #     print(arr[:idx])
    return [i for idx, i in enumerate(arr) if i in arr[:idx]]


if __name__ == "__main__":
    print(findDuplicate([1, 2, 3, 2, 4, 3, 4]))
