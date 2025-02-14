import sys

input = sys.stdin.readline

MAX_NUM = 20

# a, b, c
dp = [[[0 for _ in range(MAX_NUM + 1)] for _ in range(MAX_NUM + 1)] for _ in range(MAX_NUM + 1)]
dp[0][0][0] = 1


def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        if dp[20][20][20] == 0:
            dp[20][20][20] = w(20, 20, 20)
        return dp[20][20][20]
    if dp[a][b][c] > 0:
        return dp[a][b][c]

    if a < b < c:
        answer = w(a, b, c - 1) + w(a, b - 1, c - 1) - w(a, b - 1, c)
    else:
        answer = w(a - 1, b, c) + w(a - 1, b - 1, c) + w(a - 1, b, c - 1) - w(a - 1, b - 1, c - 1)
    dp[a][b][c] = answer
    return answer


while True:
    a, b, c = map(int, input().split())
    if a == b == c == -1:
        break
    if a <= 0 or b <= 0 or c <= 0:
        answer = 1
    elif a > 20 or b > 20 or c > 20:
        answer = w(20, 20, 20)
    elif dp[a][b][c] == 0:
        answer = w(a, b, c)
    else:
        answer = dp[a][b][c]
    print("w(" + str(a) + ", " + str(b) + ", " + str(c) + ") = " + str(answer))
