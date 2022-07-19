import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort()

result = 0
for i in range(N):
    m = max(B)
    idx = B.index(m)
    result += A[i] * m
    B.pop(idx)

print(result)
