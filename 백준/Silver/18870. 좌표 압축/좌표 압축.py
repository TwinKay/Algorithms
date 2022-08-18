import sys

n = int(sys.stdin.readline())

total = list(map(int, sys.stdin.readline().split()))
total_set = list(set(total))
total_set.sort()

dic = {}  # 시간 단축을 위해 for문 대신 dict
for i, j in enumerate(total_set):
    dic[j] = i  # k,v 반대로

for i, j in enumerate(total):
    if i + 1 == len(total):
        print(dic[j])

    else:
        print(dic[j], end=' ')