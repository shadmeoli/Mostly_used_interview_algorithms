"""
Given a list of distinct integers `nums`, return all possible subsets (the power set).

A subset is a set that can be derived by deleting zero or more elements without changing the order.

Input: [1, 2, 3]
Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]
"""

from python.tester.testLogger import test_runner


def generate_subsets(nums):
    subsets = [[]]

    for num in nums:
        new_subset = []
        for curr in subsets:
            new_subset.append(curr + [num])
        subsets.extend(new_subset)
    return subsets


@test_runner(
    expected=[[[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]], [[]], [[], [42]]],
    assert_is_array=True,
    message="Generate all subsets (power set)",
)
def test_generate_subsets(inputs):
    return generate_subsets(inputs)


if __name__ == "__main__":
    test_generate_subsets([[1, 2, 3], [], [42]])
