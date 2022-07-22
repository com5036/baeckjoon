import sys

T = int(sys.stdin.readline())

f = [0, 1, 2, 4]

for i in range(4, 11):
    f.append(f[i-1] + f[i-2] + f[i-3])

for _ in range(T):
    n = int(sys.stdin.readline())

    print(f[n])

