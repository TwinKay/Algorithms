import sys

total = []
for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().strip()
    if x[:2] == 'pu':
        a,b = x.split()
        total.append(int(b))
    else:
        if x == 'pop':
            if total != []:
                print(total.pop(-1))
            else:
                print(-1)

        elif x == 'size':
            print(len(total))

        elif x == 'empty':
            if total == []:
                print(1)
            else:
                print(0)

        else:
            if total != []:
                print(total[-1])
            else:
                print(-1)