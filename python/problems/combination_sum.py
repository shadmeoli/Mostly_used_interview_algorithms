
"""
Given an array of distinct integers `candidates` and a target integer `target`,
return all unique combinations of candidates where the chosen numbers sum up to target.

Each number in candidates can be used unlimited times.

Input: candidates = [2, 3, 6, 7], target = 7
Output: [[2, 2, 3], [7]]
"""

from python.tester.testLogger import test_runner


def combination_sum(candidates: list[int], target: int) -> list[list[int]]:
    res = []

    def backtrack(start, path, total):
        if total == target:
            res.append(list(path))
            return
        if total > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path, total + candidates[i])
            path.pop()

    backtrack(0, [], 0)
    return res


@test_runner(
    expected=[
        [[2, 2, 3], [7]],
        [[2, 2, 2, 2], [2, 3, 3], [3, 5]],
        [],
    ],
    assert_is_array=True,
    message="Combination Sum",
)
def test_combination_sum(inputs):
    return combination_sum(*inputs)


if __name__ == "__main__":
    test_combination_sum(
        [
            ([2, 3, 6, 7], 7),
            ([2, 3, 5], 8),
            ([7, 14], 3),
        ]
    )
