import sys
from collections import deque

# 3 <= N, M <= 300
# 가로, 세로
N, M = map(int, sys.stdin.readline().split())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
que = deque()
year = 0

while True:
    # print(f'=================={year}===========')
    # for tmp in m:
    #     print(tmp)

    count = 0
    visit = [[0] * M for _ in range(N)]
    c = [[0] * M for _ in range(N)]
    m_copy = []
    for tmp in m:
        m_copy.append(tmp.copy())

    for i in range(N):
        for j in range(M):
            if (m_copy[i][j] != 0) and (visit[i][j] == 0):
                visit[i][j] = 1
                que.append((i, j))

                while que:
                    x, y = que.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]

                        if nx < 0 or nx >= N or ny < 0 or ny >= M:
                            continue

                        if m_copy[nx][ny] == 0:
                            if m[x][y] > 0:
                                m[x][y] -= 1
                        else:
                            if not visit[nx][ny]:
                                visit[nx][ny] = 1
                                que.append((nx, ny))
                count += 1

    if count >= 2:
        print(year)
        exit(0)
    elif count == 0:
        print(0)
        exit(0)

    year += 1



