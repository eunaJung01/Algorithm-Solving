import sys

input = sys.stdin.readline

N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dp[0][0] = 1

for y in range(N):
    for x in range(N):
        d = board[y][x]
        if d == 0:
            continue
        if y + d < N:
            dp[y + d][x] += dp[y][x]
        if x + d < N:
            dp[y][x + d] += dp[y][x]

print(dp[N - 1][N - 1])
