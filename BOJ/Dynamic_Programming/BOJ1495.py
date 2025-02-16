import sys

input = sys.stdin.readline

N, S, M = map(int, input().split())
V = list(map(int, input().split()))

dp = [[False for _ in range(M + 1)] for _ in range(N + 1)]
dp[0][S] = True

for i in range(1, N + 1):
    for m in range(M + 1):
        if dp[i - 1][m]:
            if m - V[i - 1] >= 0:
                dp[i][m - V[i - 1]] = True
            if m + V[i - 1] <= M:
                dp[i][m + V[i - 1]] = True

answer = -1
for m in range(M, -1, -1):
    if dp[N][m]:
        answer = m
        break
print(answer)
