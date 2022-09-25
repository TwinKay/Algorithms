import sys

s = sys.stdin.readline().rstrip()
s1 = list(s.split('0'))
s2 = list(s.split('1'))
t1 = 0
for i in s1:
    if i != '':
        t1 += 1

t2 = 0
for i in s2:
    if i != '':
        t2 += 1


print(min(t1,t2))