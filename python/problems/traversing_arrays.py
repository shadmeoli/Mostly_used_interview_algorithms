"""
Given an array of integers, return the index of the
first element that is greater than or equal to 10.
If no such element exists, return -1.
"""

from python.tester.testLogger import test_runner


def find_first_big_number(arr):
    for idx, val in enumerate(arr):
        if val >= 10:
            return idx
    return -1


@test_runner(
    expected=[2, -1, 0], assert_is_array=True, message="find_first_big_number test"
)
def test_find_first_big_number(arr):
    return find_first_big_number(arr)


if __name__ == "__main__":
    test_find_first_big_number(
        [
            [2, 5, 11, 3],  # 11 is at index 2
            [1, 4, 6, 9],  # no number >= 10, return -1
            [10, 20, 30],  # 10 is at index 0
        ]
    )
