"""
Given a list of integers that might contain duplicates, return all possible subsets (the power set).
The solution must not contain duplicate subsets.

Each subset must be sorted in non-descending order, and the final result should not contain duplicate subsets.

Example:
Input: [1, 2, 2]
Output:
[
  [],
  [1],
  [1, 2],
  [1, 2, 2],
  [2],
  [2, 2]
]

Constraints:
- The input list may contain duplicates.
- You must use backtracking to build subsets.
"""

from collections import Counter
from python.tester.testLogger import test_runner


def subsets_with_duplicates(nums):
    if len(nums) > 0:
        nums = sorted(nums)
    subsets = [[]]

    for num in nums:
        new_subset = []
        for subset in subsets:
            new_subset.append(sorted([*subset, num]))
        if subsets.count(new_subset) == 0:
            subsets.extend(new_subset)

    # INFO: this is a custom trick to remove dups from the generated subsets to pass the edge case of not including dups
    tuple_subsets = [tuple(s) for s in subsets]
    unique = list(Counter(tuple_subsets).keys())
    return [list(t) for t in unique]


@test_runner(
    expected=[
        [[], [1], [2], [1, 2], [2, 2], [1, 2, 2]],
        [[], [1], [1, 1], [2], [1, 2], [1, 1, 2]],
        [[]],
    ],
    assert_is_array=True,
    message="Subsets with duplicates (backtracking)",
)
def test_subsets_with_duplicates(arr):
    return subsets_with_duplicates(arr)


if __name__ == "__main__":
    test_subsets_with_duplicates(
        [
            [1, 2, 2],
            [1, 2, 1],
            [],
        ]
    )
