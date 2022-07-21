'''
F층 건물
G층 : 스타트링크
S층 : 현재
F S G U D
1 <= S
G <= F <= 1000000
0 <= U
D <= 1000000
S에서 G로 가기 위해 눌러야하는 버튼의 수의 최소값
use the stairs
'''
import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())
visit = [0] * (F+1)

que = deque([S])

while que:
    x = que.popleft()

    for i in [U, -D]:
        if i==0:
            continue
        nx = x + i

        if nx < 1 or nx > F:
            continue

        if not visit[nx]:
            visit[nx] = visit[x] + 1
            que.append(nx)

        if nx == G:
            print(visit[nx])
            exit(0)

print("use the stairs")