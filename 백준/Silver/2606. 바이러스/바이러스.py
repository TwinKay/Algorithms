import sys

n = int(sys.stdin.readline())

total = []
for _ in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().split())
    if b<a:
        a,b = b,a
    total.append([a,b])
total.sort()

new_total = []
for i in total:
    new_total.append([i[1],i[0]])
new_total.sort()

check_list = [1]
for _ in range(100):
    for i in total:
        if i[0] in check_list:
            check_list.append(i[1])

    for j in new_total:
        if j[0] in check_list:
            check_list.append(j[1])


check_list = list(set(check_list))
print(len(check_list)-1)