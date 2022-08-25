import sys

total = []
for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().strip()
    if x[:6] == 'push_f':
        a,b = x.split()
        total.insert(0, int(b))
    elif x[:6] == 'push_b':
        a,b = x.split()
        total.append(int(b))

    else:
        if x == 'pop_front':
            if total != []:
                print(total.pop(0))
            else:
                print(-1)

        elif x == 'pop_back':
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

        elif x == 'front':
            if total != []:
                print(total[0])
            else:
                print(-1)


        else:
            if total != []:
                print(total[-1])
            else:
                print(-1)