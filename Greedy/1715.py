import heapq
import sys

n = int(sys.stdin.readline())

heap = []
tmp_result = []

for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

while True:
    if not heap:
        break
    a = heapq.heappop(heap)
    if not heap:
        break
    b = heapq.heappop(heap)

    tmp_result.append(a+b)
    heapq.heappush(heap, a+b)

print(sum(tmp_result))