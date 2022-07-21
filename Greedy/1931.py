import sys

START = 0
END = 1

MAX = 100000

n = int(sys.stdin.readline())

count = 0
result = []
time_list = []
false_list = [False for i in range(MAX)]
time_line = false_list.copy()


# 회의 시간 리스트 만들기
for i in range(n):
    tmp = list(map(int, sys.stdin.readline().split()))
    tmp.append(abs(tmp[0] - tmp[1]))
    time_list.append(tuple(tmp))

time_list.sort(key=lambda x:x[0])
time_list.sort(key=lambda x:x[1])


end = 0
for time in time_list:
    if (end <= time[START]):
        end = time[END]
        count += 1
    
print(count)
