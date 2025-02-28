import heapq
import sys

input = sys.stdin.readline

INF = int(1e9)
dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)

M, N = map(int, input().split())
maze = [list(map(int, input().strip())) for _ in range(N)]
blocks = [[INF for _ in range(M)] for _ in range(N)]

heap = []
heapq.heappush(heap, (0, 0))
blocks[0][0] = 0

while heap:
    y, x = heapq.heappop(heap)
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            continue
        if blocks[ny][nx] > blocks[y][x] + maze[ny][nx]:
            blocks[ny][nx] = blocks[y][x] + maze[ny][nx]
            heapq.heappush(heap, (ny, nx))

print(blocks[N - 1][M - 1])
