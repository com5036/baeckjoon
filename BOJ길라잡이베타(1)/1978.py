import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

result = 0
for n in nums:
    if n == 1:
        continue

    for i in range(2, n):
        if n % i == 0:
            break
    else:
        result += 1

print(result)