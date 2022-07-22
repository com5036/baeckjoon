import sys
from itertools import combinations

while True:
    tmp = list(map(int, sys.stdin.readline().split()))
    K = tmp[0]
    if K == 0:
        break
    S = tmp[1:]

    for r in list(combinations(S, 6)):
        print(*r)
    print()