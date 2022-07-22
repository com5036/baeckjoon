import sys

n = int(sys.stdin.readline())

lst = [int(sys.stdin.readline()) for _ in range(n)]

stack = []
make_lst = []
result = []
i, j = 1, 0

while i <= n:
    stack.append(i)
    result.append('+')
    i += 1

    while stack and stack[-1] == lst[j]:
        make_lst.append(stack.pop())
        result.append('-')
        j += 1

if make_lst == lst:
    print('\n'.join(result))
else:
    print("NO")




