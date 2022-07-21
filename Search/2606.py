import collections
import sys


def bfs(start):
    que = collections.deque()
    que.append(start)

    while que:
        x = que.popleft()

        if x not in virus:
            virus.append(x)
            for com in net[x]:
                que.append(com)

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())

net = collections.defaultdict(list)
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    net[a].append(b)
    net[b].append(a)

virus = []

bfs(1)
print(len(virus)-1)

