import sys

n = int(sys.stdin.readline())

lst = [int(sys.stdin.readline()) for _ in range(n)]

stack = [1]
make_lst = []
result = ['NO', '+']
i, j = 2, 0

while i <= n:
    if lst[j] != stack[-1]:
        stack.append(i)
        result.append('+')
        i += 1

    else:
        p = stack.pop()
        make_lst.append(p)
        result.append('-')
        j += 1

if make_lst == lst:
    print('\n'.join(result[1:]))
else:
    print(result[0])
