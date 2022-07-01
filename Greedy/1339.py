import sys
from collections import defaultdict

# input
n = int(sys.stdin.readline())
word_list = [sys.stdin.readline().strip() for i in range(n)]

word_by_num = dict()
dic = defaultdict(list)

# 자리수 별로 문자 정리 
for word in word_list:
    i = 1
    for w in word[::-1]:
        dic[i].append(w)
        i += 1
        

# 갯수 추가
non_overlap_list = []
for i in range(8, 0, -1):
    val_list = dic[i]
    non_overlap_list = list(set(val_list))
    
    for ch in non_overlap_list:
        idx = non_overlap_list.index(ch)
        non_overlap_list[idx] = (ch, val_list.count(ch))

    dic[i] = non_overlap_list


# 갯수 기준 정렬
for val in dic.values():
    val.sort(key= lambda x:x[1], reverse=True)



# 문자를 숫자로 변환
num = 9
for i in range(8, 0, -1):
    val = dic[i]
    
    for v in val:
        if v[0] not in word_by_num:
            word_by_num[v[0]] = num
            num -= 1

# 합
result = 0
for key, val_list in dic.items():
    t = 10 ** (key-1)
    for v in val_list:
        result += word_by_num[v[0]] * v[1] * t

print(result)
