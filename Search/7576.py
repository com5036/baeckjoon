import sys
from collections import deque

# 가로, 세로
m, n = map(int, sys.stdin.readline().split())
box = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)
result = 0
ripe_tomato_pos = deque()

# 익은 토마토 좌표, 개수
# 빈 공간 개수
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            ripe_tomato_pos.append((i, j))

# 시뮬레이션
while ripe_tomato_pos:
    x, y = ripe_tomato_pos.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx >= n or ny >= m or box[nx][ny] == -1 or box[nx][ny] == 1:
            continue

        if box[nx][ny] == 0:
            box[nx][ny] = box[x][y] + 1
            ripe_tomato_pos.append((nx, ny))

breaker = False
for i in range(n):
    if breaker: break
    for j in range(m):
        if box[i][j] == 0:
            result = 0
            breaker = True
            break
        result = max(result, box[i][j])

print(result-1)
