import sys
from collections import deque

#가로, 세로, 높이
M, N, H = map(int, sys.stdin.readline().split())

box = list()
for _ in range(H):
    tmp = list()
    for _ in range(N):
        tmp.append(list(map(int,sys.stdin.readline().split())))
    box.append(tmp)

dx = (0, 0, 1, -1, 0, 0)
dy = (1, -1, 0, 0, 0, 0)
dz = (0, 0, 0, 0, 1, -1)

ripe_tomato_pos = deque()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 1:
                ripe_tomato_pos.append((i, j, k))

ripe_tomato_count = len(ripe_tomato_pos)

result = 0

while ripe_tomato_pos:
    x, y, z = ripe_tomato_pos.popleft()

    for i in range(6):
        nx = x + dx[i]
        ny = y + dy[i]
        nz = z + dz[i]

        if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and box[nx][ny][nz] == 0:
            box[nx][ny][nz] = box[x][y][z] + 1
            ripe_tomato_pos.append((nx, ny, nz))


for i in range(H):
    for j in range(N):
        for k in range(M):
            if box[i][j][k] == 0:
                print(-1)
                exit(0)
            result = max(box[i][j][k], result)


print(result-1)