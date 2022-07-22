import sys
from itertools import combinations

N, S = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

result = 0
for i in range(1, N+1):
    subset = list(combinations(nums, i))
    for s in subset:
        if S == sum(s):
            result += 1

print(result)