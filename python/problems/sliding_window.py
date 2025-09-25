"""
Given a string `s`, return the length of the **longest substring**
without repeating characters.

You must use a sliding window approach.

Examples:
Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Input: "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Note that the answer must be a substring, "pwke" is a subsequence and not a valid answer.
"""

from collections import Counter

from python.tester.testLogger import test_runner


def length_of_longest_substring(s):
    _set = set()
    step = 0
    left = 0

    for right in range(len(s)):
        while s[right] in _set:
           _set.remove(s[left])
           left += 1

        window = (right - left) + 1
        step = max(step, window)
        _set.add(s[right])

    return step

@test_runner(
    expected=[3, 1, 3, 0, 2, 6],
    assert_is_array=True,
    message="Sliding window: longest substring without repeating characters",
)
def test_length_of_longest_substring(arr):
    return length_of_longest_substring(arr)


if __name__ == "__main__":
    test_length_of_longest_substring(
        [
            "abcabcbb",  # "abc"
            "bbbbb",  # "b"
            "pwwkew",  # "wke"
            "",  # ""
            "aab",  # "ab"
            "abcdef",  # "abcdef"
        ]
    )
