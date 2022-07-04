'''
d(75) = 75+7+5 = 87
n: d(n)의 생성자, 33은 39의 생성자
생성자가 없는 숫자를 셀프 넘버
10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력
'''

def d(n):
    result = n
    for i in str(n):
        result += int(i)

    return result


num_list = [i for i in range(1, 10000)]

for i in range(10000):
    d_i = d(i)
    if d_i in num_list:
        num_list.remove(d_i)

for n in num_list:
    print(n)
