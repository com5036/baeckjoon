import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

miro = []
for _ in range(n):
    miro.append(list(map(int, sys.stdin.readline().strip())))

# 오른쪽, 아래, 왼쪽, 위
dx = (0, 1, 0, -1)
dy = (1, 0, -1, 0)


def bfs(x, y):
    que = deque()
    que.append((x, y))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue

            if miro[nx][ny] == 0:
                continue

            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                que.append((nx, ny))

    return miro[n-1][m-1]


result = bfs(0, 0)
print(result)

