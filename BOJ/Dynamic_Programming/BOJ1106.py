import sys

input = sys.stdin.readline

INF = int(1e9)

C, N = map(int, input().split())
monies = []
customers = []
for _ in range(N):
    m, c = map(int, input().split())
    monies.append(m)
    customers.append(c)

max_C = C + max(customers)
dp = [[INF for _ in range(max_C + 1)] for _ in range(N + 1)]

for i in range(1, N + 1):
    money = monies[i - 1]
    customer = customers[i - 1]
    for j in range(1, max_C + 1):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        if j < customer:
            continue
        if j == customer:
            dp[i][j] = min(dp[i][j], money)
        dp[i][j] = min(dp[i][j], dp[i][j - customer] + money)
        dp[i][j] = min(dp[i][j], dp[i - 1][j - customer] + money)

print(min(dp[N][C:max_C + 1]))
