import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

que = deque()
que.append(n)
visit = [0] * 100001


while que:
    x = que.popleft()
    if x == k:
        print(visit[x])
        exit(0)

    for nx in [x-1, x+1, x*2]:
        if 0 <= nx <= 100000 and not visit[nx]:
            visit[nx] = visit[x] + 1
            que.append(nx)



