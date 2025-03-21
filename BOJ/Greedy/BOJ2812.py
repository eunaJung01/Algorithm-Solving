import sys

input = sys.stdin.readline

N, K = map(int, input().split())
number = list(map(int, input().strip()))

stack = []
for num in number:
    while stack and K > 0 and stack[-1] < num:
        stack.pop()
        K -= 1
    stack.append(num)

print(''.join(map(str, stack[:len(stack) - K])))
