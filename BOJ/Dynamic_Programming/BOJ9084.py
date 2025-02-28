import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    amounts = list(map(int, input().split()))
    M = int(input())

    dp = [[0 for _ in range(M + 1)] for _ in range(N + 1)]
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            amount = amounts[i - 1]
            if j < amount:
                dp[i][j] = dp[i - 1][j]
                continue
            if amount == j:
                dp[i][j] += 1
            dp[i][j] += dp[i - 1][j]
            dp[i][j] += dp[i][j - amount]

    print(dp[N][M])
