import sys

result = 0
n = int(sys.stdin.readline())

while (n % 5 != 0):
    n -= 3
    result += 1

while ( n > 0):
    n -= 5
    result += 1

if (n != 0):
    result = -1
    
print(result)
    
    
