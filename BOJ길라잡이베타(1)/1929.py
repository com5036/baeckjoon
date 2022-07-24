'''
소수 : 약수가 1과 자기자신

'''
import sys


def isPrime(num):
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    else:
        return True


M, N = map(int, sys.stdin.readline().split())

for num in range(M, N+1):
    if isPrime(num) and num != 1:
        print(num)

