'''
L : 왼쪽
D : 오른쪽
B : 왼쪽 삭제
P $ : '$' 커서 왼쪽에 추가
'''

import sys
import collections

st1 = list(sys.stdin.readline().strip()) # 커서 기준 왼쪽
M = int(sys.stdin.readline())
st2 = [] # 커서기준 오른쪽
for _ in range(M):
    op = sys.stdin.readline().strip().split()

    if op[0] == 'L':
        if st1:
            st2.append(st1.pop())
    elif op[0] == 'D':
        if st2:
            st1.append(st2.pop())
    elif op[0] == 'B':
        if st1:
            st1.pop()
    elif op[0] == 'P':
        st1.append(op[1])


print(''.join(st1), end='')
print(''.join(st2[::-1]))