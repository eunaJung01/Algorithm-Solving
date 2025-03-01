import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 5)

N, M, R = map(int, input().split())

edges = [[] for _ in range(N + 1)]
for _ in range(M):
    u, v = map(int, input().split())
    edges[u].append(v)
    edges[v].append(u)
for e in edges:
    e.sort()

orders = [0 for _ in range(N + 1)]
cnt = 1


def dfs(node):
    global cnt
    orders[node] = cnt
    cnt += 1
    for next_node in edges[node]:
        if orders[next_node] > 0:
            continue
        dfs(next_node)


dfs(R)
for order in orders[1:]:
    print(order)
