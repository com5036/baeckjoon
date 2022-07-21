import sys
from collections import deque


def bfs(start):
    global n, t

    count = 0
    que = deque()
    que.append(start)

    while que:
        x, y = que.popleft()

        if city[x][y] == 1:
            city[x][y] = 0
            count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue

            if city[nx][ny] == 1:
                if (nx, ny) not in que:
                    que.append((nx, ny))

    return count

n = int(sys.stdin.readline())
city = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]

# 위, 오른쪽, 아래, 왼쪽
dx = (-1, 0, 1, 0)
dy = (0, 1, 0, -1)

result = []
for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            result.append(bfs((i, j)))

result.sort()

print(len(result))
for r in result:
    print(r)


