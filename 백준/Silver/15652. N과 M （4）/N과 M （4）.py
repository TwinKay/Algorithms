import sys

def make_num_lsts(lst):
    temp = []
    for i in num_range:
        if i >= lst[-1]:
            temp.append(lst+[i])
    return temp

n,m = map(int, sys.stdin.readline().split())

num_range = list(range(1,n+1))
res = []
for i in num_range:
    res.append([i])

temp = []
for rp in range(m-1):
    for i in res:
        temp.extend(make_num_lsts(i))
    res = temp
    temp = []

for i in res:
    i = list(map(str,i))
    print(' '.join(i))