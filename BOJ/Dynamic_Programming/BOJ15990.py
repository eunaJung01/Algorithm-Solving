import sys

input = sys.stdin.readline

MOD = 1_000_000_009

T = int(input())
nums = list(int(input()) for _ in range(T))

dp = [[0 for _ in range(3)] for _ in range(max(nums) + 1)]
dp[1][0] = 1
dp[2][1] = 1
dp[3][0] = dp[3][1] = dp[3][2] = 1

for i in range(4, max(nums) + 1):
    dp[i][0] = (dp[i - 1][1] + dp[i - 1][2]) % MOD
    dp[i][1] = (dp[i - 2][0] + dp[i - 2][2]) % MOD
    dp[i][2] = (dp[i - 3][0] + dp[i - 3][1]) % MOD

for n in nums:
    print((dp[n][0] + dp[n][1] + dp[n][2]) % MOD)
