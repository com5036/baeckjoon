import sys
from collections import defaultdict

n = int(sys.stdin.readline())
p1, p2 = map(int, sys.stdin.readline().split())
m = int(sys.stdin.readline())

graph = defaultdict(list)
for i in range(m):
    parent, child = map(int, sys.stdin.readline().split())
    graph[parent].append(child)
    graph[child].append(parent)


visit = []


def dfs(start, count):
    visit.append(start)
    if p2 in graph[start]:
        print(count)
        exit(0)

    for g in graph[start]:
        if g not in visit:
            dfs(g, count + 1)


dfs(p1, 1)
print(-1)