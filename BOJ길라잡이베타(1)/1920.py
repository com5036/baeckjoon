import sys

n = int(sys.stdin.readline())
nums = sys.stdin.readline().strip().split()
m = int(sys.stdin.readline())
check = sys.stdin.readline().strip().split()

nums.sort()
start = 0
end = n
mid = n // 2

for c in check:
    start = 0
    end = n
    while start < end:
        mid = (start + end) // 2
        if nums[mid] == c:
            print(1)
            break
        elif nums[mid] < c:
            start = mid+1
        elif nums[mid] > c:
            end = mid
        else:
            print(0)
            break
    else:
        print(0)
