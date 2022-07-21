import sys
from collections import deque
N = int(sys.stdin.readline())
m = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

rain = 0
for v in m:
    rain = max(v) if max(v) > rain else rain

dx = (0, 0, 1, -1)
dy = (1, -1, 0, 0)
count_list = []
for r in range(rain+1):
    que = deque([(0, 0)])
    visit = [[0] * N for _ in range(N)]

    count = 0
    m_copy = m.copy()

    # r이하 물에 잠기게 0으로 표시
    for i in range(N):
        for j in range(N):
            if m_copy[i][j] <= r:
                m_copy[i][j] = 0
    
    # 안전 영역 표시
    for i in range(N):
        for j in range(N):
            if not visit[i][j] and m_copy[i][j] != 0:
                visit[i][j] = 1
                que.append((i, j))
                while que:
                    x, y = que.popleft()
                    for k in range(4):
                        nx = x + dx[k]
                        ny = y + dy[k]
                        if (0 <= nx < N) and (0 <= ny < N) and (m_copy[nx][ny] != 0) and not visit[nx][ny]:
                            visit[nx][ny] = 1
                            que.append((nx, ny))

                count += 1

    count_list.append(count)


print(max(count_list))





