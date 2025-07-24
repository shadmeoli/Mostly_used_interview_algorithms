"""
Given an array of integers, return the indices of all elements
that are greater than both their neighbors. These are called "peaks".

Notes:
- The first and last elements are never considered peaks.
- An element is a peak if: arr[i] > arr[i - 1] and arr[i] > arr[i + 1]

Example:
Input: [1, 3, 2, 4, 1, 5, 2]
Output: [1, 3, 5]
Explanation:
  - 3 > 1 and 3 > 2 → index 1 is a peak
  - 4 > 2 and 4 > 1 → index 3 is a peak
  - 5 > 1 and 5 > 2 → index 5 is a peak
"""

from python.tester.testLogger import test_runner


def find_peaks(arr):
    peaks = []
    # O(n) -> time
    for idx in range(1, len(arr) - 1):
        # O(1) -> space
        if arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]:
            peaks.append(idx)
    return peaks


@test_runner(
    expected=[[1, 3, 5], [], [2], [1]],  # All expected results now match input count
    assert_is_array=True,
    message="Find peak indices",
)
def test_find_peaks(arr):
    return find_peaks(arr)


if __name__ == "__main__":
    test_find_peaks(
        [
            [1, 3, 2, 4, 1, 5, 2],  # peaks at 3, 4, 5 → indices: [1, 3, 5]
            [1, 2, 3, 4, 5],  # strictly increasing → no peaks
            [5, 4, 9, 2, 1],  # peak at 9 → index 2
            [1, 3, 2, 4, 5],  # peak at 3 → index 1
        ]
    )
