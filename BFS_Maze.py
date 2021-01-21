import time
from collections import deque

n, m = map(int, input().split())
maze = []
count = 0

for _ in range(n):
    maze.append(list(map(int, input())))

start_time = time.time()

# 상 하 좌 우
dx = [-1, 1, 0, 0]      # n
dy = [0, 0, -1, 1]      # m


def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    while queue:
        x, y = queue.popleft()
        for o in range(4):
            nx = x + dx[o]
            ny = y + dy[o]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if maze[nx][ny] == 0:
                continue
            if maze[nx][ny] == 1:
                maze[nx][ny] = maze[nx][ny] + 1
                queue.append((nx, ny))

    return maze[n - 1][m - 1]


bfs(0, 0)

for i in range(n):
    for j in range(m):
        if maze[i][j] == 2:
            count = count + 1

end_time = time.time()

print(count)
print(maze)
print("소요시간 :", end_time - start_time)
