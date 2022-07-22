import sys

N, K = map(int, sys.stdin.readline().split())

people = list(range(1, N+1))
result = []
idx = 0

while people:
    idx += (K-1)

    if idx >= N:
        idx = idx % N

    p = people.pop(idx)
    result.append(str(p))
    N -= 1

print('<', end='')
print(', '.join(result), end='')
print('>', end='')
