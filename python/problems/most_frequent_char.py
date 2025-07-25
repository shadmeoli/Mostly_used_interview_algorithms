"""
Given a string, return the character that appears the most frequently.
If multiple characters have the same highest frequency, return the one that appears first in the string.

Example:
Input: "abcaabcc"
Output: "a"  # 'a' appears 3 times, which is the highest
"""

from collections import Counter

from python.tester.testLogger import test_runner


def most_frequent_char(s):
    freq = Counter(s)
    max_val = max(list(freq.values()))
    ans = ""

    for key, value in freq.items():
        if value == max_val:
            ans = key
            break
    return ans


@test_runner(
    expected=["b", "l", "e"],
    assert_is_array=True,
    message="Most frequent character",
)
def test_most_frequent_char(arr):
    return most_frequent_char(arr)


if __name__ == "__main__":
    test_most_frequent_char(
        [
            "abcabbbabcc",  # 'a' appears 3 times
            "levelupskills",  # 'l' appears 3 times
            "edgecase",  # 'e' appears 2 times first
        ]
    )
