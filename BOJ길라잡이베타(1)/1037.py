import sys

'''
N이 A의 배수
A는 1과 N이 아니어야함
'''
len_A = sys.stdin.readline()
A = list(map(int, sys.stdin.readline().split()))

print(max(A) * min(A))