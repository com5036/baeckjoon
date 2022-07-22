'''
R: 배열 뒤집기
D: 0번째 버리기, 비어있는데 사용하면 에러

'''
import sys
from collections import deque

for _ in range(int(sys.stdin.readline())):
    r = False
    p = sys.stdin.readline()
    n = int(sys.stdin.readline())

    arr = sys.stdin.readline()[1:-2]
    if arr != '':
        arr = arr.split(',')
    arr = deque(arr)

    # 명령 실행
    for op in p:
        if op == 'R':
            r = not r
        elif op == 'D':
            if not arr:
                print('error')
                break
            if r:
                arr.pop()
            else:
                arr.popleft()
    else:
        print('[', end='')
        if r:
            arr.reverse()
            print(','.join(list(arr)), end='')
        else:
            print(','.join(list(arr)), end='')
        print(']')