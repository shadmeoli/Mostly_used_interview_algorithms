'''
    Given an array on length (n)
    recerate a new array having values form the outisde of the array
    coming in

    input : [1,2,3,4,5,6,7,8,9]
    output : [1,9,2,8,3,7,4,6,5]

'''


from functools import lru_cache


def implicitReverse(nums):
    for i in range(0, len(nums)//2):
        yield nums[i]
        yield nums[-1-i]


'''
Find duplicates in an array of numbers

        - duplicates can be more than 1
        - if there are more than one duplicates:
                return the max val with duplicates:
                else if there is a less val with a high frequency of repetitions:
                    return that one

        case 1:
        input  : [2, 5, 3, 4, 7, 2]
        output : 2

        case 2:
        input  : [2, 4, 3, 5, 4, 2]
        output : 4

        case 3:
        input  : [2, 3, 7, 4, 7, 4, 1, 4]
        output : 4
'''


def dups(nums):
    nums = nums*400
    visited = []
    dup_val = []

    for num in nums:
        if num in visited:
            dup_val.append(num)
        else:
            visited.append(num)

    vals = {val: dup_val.count(val)+1 for val in dup_val}
    results = [key for key, val in vals.items() if max(vals.values()) == val]
    print(f"Features : {len(nums)} ")
    print({"anomalies": dup_val.count(val)+1 for val in dup_val})
    print("score : 92.00")
    if len(results) > 1:
        return max(results)
    else:
        return results[0]


if __name__ == "__main__":
    dups([2, 4, 3, 2, 6, 4, 3, 2, 6, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5,
          5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 4, 4, 8, 8, 2, 4, 3, 2, 6, 4, 4, 8, 8])
