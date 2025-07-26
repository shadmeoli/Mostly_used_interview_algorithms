"""
Given a non-negative integer n, return the sum of its digits using recursion.

Examples:
sum_digits(1234) → 10
sum_digits(999) → 27
"""

from python.tester.testLogger import test_runner


def sum_digits(n):
    n = str(n)
    total = 0
    for i in range(len(n)):
        total += int(n[i])
        print("Total", total)
    return total


def recursive_sum_digits(n, i=0, total=0):
    if i == len(str(n)):
        return total
    return recursive_sum_digits(n, i + 1, total + int(str(n)[i]))


@test_runner(
    expected=[10, 27, 0, 7, 5],
    assert_is_array=True,
    message="Sum of digits using recursion",
)
def test_sum_digits(arr):
    return recursive_sum_digits(arr)


if __name__ == "__main__":
    test_sum_digits([1234, 999, 0, 7, 104])
