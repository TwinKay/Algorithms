import sys

s = sys.stdin.readline().rstrip()
s = s.upper()
map = {}
for c in s:
    map[c] = map.setdefault(c,0)+1

lst = []
for key in map.keys():
    lst.append([map[key],key])
lst.sort(reverse=True)
if len(lst)==1:
    print(lst[0][1])
else:
    if lst[0][0] == lst[1][0]:
        print("?")
    else:
        print(lst[0][1])