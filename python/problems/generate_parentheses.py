"""
Given `n` pairs of parentheses, write a function that generates all combinations of **well-formed** parentheses.

Constraints:
- 1 <= n <= 8

Example:
Input:  n = 3
Output: ["((()))", "(()())", "(())()", "()(())", "()()()"]

Explanation:
Each string must contain `n` opening and `n` closing parentheses, in a valid order.
"""
from types import SimpleNamespace
from python.tester.testLogger import test_runner


def generate_parentheses(n: int) -> list[str]:
    map = SimpleNamespace(**{
        "open": "(",
        "close" : ")"
    })
    res = []


    # if n == 0:
    #     return []

    # if n == 1:
    #     return [map.open+map.close]

    def backtrack(open, close, path):

        if len(path) == 2*n:
            res.append("".join(path))
            return

        if open < n:
            path.append(map.open)
            backtrack(open+1, close, path)
            path.pop()

        if close < open:
            path.append(map.close)
            backtrack(open, close+1, path)
            path.pop()

    backtrack(0, 0, [])
    return res


@test_runner(
    expected=[
        ["()"],
        ['(())', '()()'],
        ["((()))", "(()())", "(())()", "()(())", "()()()"],
    ],
    assert_is_array=True,
    message="Generate all valid parentheses combinations",
)
def test_generate_parentheses(arr):
    return generate_parentheses(arr)


if __name__ == "__main__":
    test_generate_parentheses([1, 2, 3])
