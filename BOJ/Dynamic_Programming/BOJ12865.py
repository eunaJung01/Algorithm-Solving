import sys

input = sys.stdin.readline

N, K = map(int, input().split())
W = []
V = []
for _ in range(N):
    w, v = map(int, input().split())
    W.append(w)
    V.append(v)

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for n in range(1, N + 1):
    for k in range(1, K + 1):
        w = W[n - 1]
        v = V[n - 1]
        if w > k:
            dp[n][k] = dp[n - 1][k]
        else:
            dp[n][k] = max(dp[n - 1][k], dp[n - 1][k - w] + v)

print(dp[N][K])
