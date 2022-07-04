import sys
from itertools import combinations

EMPTY = 0
HOUSE = 1
CHICKEN = 2

n, m = map(int, sys.stdin.readline().rstrip().split())

city = []
for _ in range(n):
    city.append(list(map(int, sys.stdin.readline().rstrip().split())))

house_pos = []
chicken_pos = []
for i in range(n):
    for idx, val in enumerate(city[i]):
        if val == HOUSE:
            house_pos.append((i, idx))
        if val == CHICKEN:
            chicken_pos.append((i, idx))

p_chicken_pos = list(combinations(chicken_pos, m))

result_list = []
result = 0
min_distance = 999

for select in range(len(p_chicken_pos)):
    # select : (((3, 0), (4, 0)))
    for h in house_pos:
        # h: (1, 3)
        for c in p_chicken_pos[select]:
            # c: (4,4)
            d = abs(h[0] - c[0]) + abs(h[1] - c[1])
            min_distance = d if d < min_distance else min_distance

        result += min_distance
        min_distance = 999

    result_list.append(result)
    result = 0
    min_distance = 999

print(min(result_list))

'''
N x N 도시

도시(r, c)

빈 칸: 0
집: 1
치킨 집: 2
+
치킨 거리: 집과 가장 가까운 치킨집 사이의 거리
도시의 치킨 거리: 모든 치킨 거리의 합

5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

'''