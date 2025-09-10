def largetSquare(farm: list[list[int]]) -> int:
    n = len(farm)
    m = len(farm[0])
    dp = [[n] * 0 for i in range(m)]
    max_num = -1
    for i in range(n - 1):
        for j in range(m - 1):
            if farm[i][j] == 0:
                continue
            left = right = diag = 0
            if i > 0:
                left = dp[i - 1][j]
            if j > 0:
                right = dp[i][j - 1]
            if i > 0 and j > 0:
                diag = dp[i - 1][j - 1]
            dp[i][j] = min([left, right, diag]) + 1
            max_num = max(max_num, dp[i][j])
    return max_num


if __name__ == "__main__":
    farm = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 1],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0],
    ]
    print(largetSquare(farm))
