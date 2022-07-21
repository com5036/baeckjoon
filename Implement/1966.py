import sys

test_num = int(sys.stdin.readline())


for i in range(test_num):
    n, m = map(int, sys.stdin.readline().split())
    priority = list(map(int, sys.stdin.readline().rstrip().split()))

    que = []
    for j in range(n):
        que.append((priority[j], j))

    cnt = 1
    while que:
        if que[0][0] >= max(que, key=lambda x: x[0])[0]:
            if que[0][1] == m:
                print(cnt)

            que.remove(que[0])
            cnt += 1
        else:
            que.append(que[0])
            que.remove(que[0])
