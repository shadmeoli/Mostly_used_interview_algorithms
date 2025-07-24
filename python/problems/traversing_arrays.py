"""
Given an array of integers, return the index of the
first element that is greater than or equal to 10.
If no such element exists, return -1.
"""

from python.tester.testLogger import test_runner


# level 1
def find_first_big_number(arr):
    # O(n)
    for idx, val in enumerate(arr):
        if val >= 10:
            return idx
    return -1


@test_runner(
    expected=[2, -1, 0], assert_is_array=True, message="Finding bing number's index"
)
def test_find_first_big_number(arr):
    return find_first_big_number(arr)


# level 2
def count_increasing_pairs(arr):
    adj = 0
    # time O(n)
    for idx, val in enumerate(arr):
        # space O(1)
        if idx == 0:
            continue
        # space O(1)
        if val > arr[idx - 1]:
            adj += 1
    return adj


@test_runner(
    expected=[3, 0, 1], assert_is_array=True, message="Counting increasing pairs"
)
def test_count_increasing_pairs(arr):
    return count_increasing_pairs(arr)


if __name__ == "__main__":
    # test_find_first_big_number(
    #     [
    #         [2, 5, 11, 3],  # 11 is at index 2
    #         [1, 4, 6, 9],  # no number >= 10, return -1
    #         [10, 20, 30],  # 10 is at index 0
    #     ]
    # )

    test_count_increasing_pairs(
        [
            [1, 3, 2, 4, 6],  # (1,3), (2,4), (4,6) → 3
            [9, 7, 5, 3],  # strictly decreasing → 0
            [5, 5, 6],  # only (5,6) → 1
        ]
    )
