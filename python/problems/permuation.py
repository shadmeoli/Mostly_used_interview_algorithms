from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    results = []

    # base classmethod
    if len(nums) == 1:
        return [nums.copy()]  # make it faster with a copying macro [nums[:]]

    for num in nums:
        variant = [num]
        for val in nums:
            if val == num:
                continue
            variant.append(val)
        if variant == nums:
            continue
        results.append(variant)

    return results


print(permute([4, 5, 6]))
print(permute([1, 2, 3]))
