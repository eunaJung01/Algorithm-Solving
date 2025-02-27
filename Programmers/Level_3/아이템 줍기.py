from collections import deque

dy = (-1, 1, 0, 0)
dx = (0, 0, -1, 1)


def solution(rectangle, characterX, characterY, itemX, itemY):
    n = 0
    for r in rectangle:
        n = max(n, max(r))
    n *= 2

    grid = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    for lower_left_x, lower_left_y, upper_right_x, upper_right_y in rectangle:
        lower_left_x *= 2
        lower_left_y *= 2
        upper_right_x *= 2
        upper_right_y *= 2
        for i in range(lower_left_y, upper_right_y + 1):
            for j in range(lower_left_x, upper_right_x + 1):
                if i == lower_left_y or j == lower_left_x or i == upper_right_y or j == upper_right_x:
                    if grid[i][j] < 2:
                        grid[i][j] = 1
                    continue
                grid[i][j] = 2

    q = deque()
    q.append((characterY * 2, characterX * 2))
    visited = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    visited[characterY * 2][characterX * 2] = 1

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if ny < 0 or ny > n or nx < 0 or nx > n or visited[ny][nx]:
                continue
            if grid[ny][nx] == 1:
                visited[ny][nx] = visited[y][x] + 1
                q.append((ny, nx))
    return int((visited[itemY * 2][itemX * 2] - visited[characterY * 2][characterX * 2]) / 2)
