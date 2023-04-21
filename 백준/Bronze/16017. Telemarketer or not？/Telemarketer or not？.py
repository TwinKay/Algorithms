import sys

l = []
for _ in range(4):
    l.append(int(sys.stdin.readline()))
if l[0] in [8,9] and l[-1] in [8,9] and l[1]==l[2]:
    print('ignore')
else:
    print('answer')
