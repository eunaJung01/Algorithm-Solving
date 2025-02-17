import sys

input = sys.stdin.readline

N = int(input())
M = int(input())
VIP = [int(input()) for _ in range(M)]

ranges = []
prev = 0
for v in VIP:
    ranges.append(v - prev - 1)
    prev = v
ranges.append(N - prev)

dp = [0 for _ in range(41)]
dp[1] = 1
dp[2] = 2
for i in range(3, 41):
    dp[i] = dp[i - 1] + dp[i - 2]

answer = 1
for r in ranges:
    if r > 0:
        answer *= dp[r]
print(answer)
