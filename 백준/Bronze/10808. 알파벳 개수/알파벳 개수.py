import sys, string

s = sys.stdin.readline().rstrip()
total = string.ascii_lowercase
dic = {}
for i in total:
    dic[i] = 0
for i in s:
    dic[i] += 1

res = list(dic.values())
res = list(map(str, res))
print(' '.join(res))