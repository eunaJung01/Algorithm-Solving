import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)

V, E = map(int, input().split())
K = int(input())
edges = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    edges[u].append((v, w))

heap = []
heapq.heappush(heap, (0, K))

dp = [INF for _ in range(V + 1)]
dp[K] = 0

while heap:
    _, node = heapq.heappop(heap)
    for next_node, weight in edges[node]:
        if dp[next_node] > dp[node] + weight:
            dp[next_node] = dp[node] + weight
            heapq.heappush(heap, (dp[next_node], next_node))

for i in range(1, V + 1):
    if dp[i] == INF:
        print("INF")
        continue
    print(dp[i])
