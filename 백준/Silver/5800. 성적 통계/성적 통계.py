import sys

n = int(sys.stdin.readline())

for i in range(n):
    print("Class", i+1)

    total = list(map(int, sys.stdin.readline().split()))
    a = total[0]
    total.remove(a)
    total.sort()

    near = []
    for i in range(len(total)-1):
        near.append(total[i+1]-total[i])

    print('Max '+str(total[-1])+','+' Min '+str(total[0])+','+' Largest gap '+str(max(near)))