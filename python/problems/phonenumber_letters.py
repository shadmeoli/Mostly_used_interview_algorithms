"""
Problem: Letter Combinations of a Phone Number

Given a string containing digits from `2` to `9`, return all possible letter combinations
that the number could represent based on the classic telephone keypad mapping.

📱 Mapping:
- 2 → "abc"
- 3 → "def"
- 4 → "ghi"
- 5 → "jkl"
- 6 → "mno"
- 7 → "pqrs"
- 8 → "tuv"
- 9 → "wxyz"

Example:
Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

Notes:
- Return an empty list if the input is an empty string.
- Use backtracking to generate the combinations.
"""

from ast import comprehension
from python.tester.testLogger import test_runner


def letter_combinations(digits):
    digits = str(digits)
    mapping = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    combinations = []

    if not digits:
        return []

    def backtrack(index, path):
        if index == len(digits):
            combinations.append("".join(path))
            return

        for char in mapping[digits[index]]:
            path.append(char)
            backtrack(index+1, path)
            path.pop()

    backtrack(0, [])
    return combinations

@test_runner(
    expected=[
        ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],  # for "23"
        [],  # for ""
        ["a", "b", "c"],  # for "2"
    ],
    assert_is_array=True,
    message="Phone number letter combinations",
)
def test_letter_combinations(arr):
    return letter_combinations(arr)


if __name__ == "__main__":
    test_letter_combinations(["23", "", "2"])
