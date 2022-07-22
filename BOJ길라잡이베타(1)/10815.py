import sys

N = int(sys.stdin.readline())
card = list(sys.stdin.readline().strip().split())
M = int(sys.stdin.readline())
check = list(sys.stdin.readline().strip().split())

card.sort()

for c in check:
    start = 0
    end = N
    while start < end:
        mid = (start + end) // 2
        if c == card[mid]:
            print(1, end=' ')
            break
        elif c < card[mid]:
            end = mid
        elif c > card[mid]:
            start = mid + 1
        else:
            print(0, end=' ')
            break
    else:
        print(0, end=' ')
