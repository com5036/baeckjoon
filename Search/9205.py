'''
한박스 20개
50미터에 한 병

'''
import sys


t = int(sys.stdin.readline())
for _ in range(t):
    # =====입력=============
    # 편의점 개수
    n = int(sys.stdin.readline())

    # 집
    home_x, home_y = map(int, sys.stdin.readline().split())

    # 편의점
    store_x = []
    store_y = []
    for i in range(n):
        store_x[i], store_y[i] = map(int, sys.stdin.readline().split())

    # 펜타포트 락 페스티벌
    pentar_x, pentar_y = map(int, sys.stdin.readline().split())

    # ========= ===============

    # ======== 출력 =========
    print(result)