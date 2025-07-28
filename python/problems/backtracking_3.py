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
- Use recursion
"""

from python.tester.testLogger import test_runner


def subsets_with_recursion(nums):
    n = len(nums)
    subsets, subset_value = [], []
    def backtrack(i):
        if i == n:
            subsets.append(subset_value.copy())
            return
        
        backtrack(i+1)
        subset_value.append(nums[i])
        backtrack(i+1)
        subset_value.pop()

    backtrack(0)
    return subsets


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
    return subsets_with_recursion(arr)


if __name__ == "__main__":
    test_subsets_with_duplicates(
        [
            [1, 2, 2],
            [1, 2, 1],
            [],
        ]
    )
