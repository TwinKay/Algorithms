import sys

result = set()
all_set = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
empty_set = set()

for _ in range(int(sys.stdin.readline())):
    x = sys.stdin.readline().strip()

    if x == 'all':
        result = all_set


    elif x == 'empty':
        result = empty_set


    else:
        a, b = x.split()
        b = int(b)

        if a == 'add':
            if b not in result:
                result.add(b)

        elif a == 'remove':
            if b in result:
                result.remove(b)

        elif a == 'check':
            if b in result:
                print(1)
            else:
                print(0)

        elif a == 'toggle':
            if b in result:
                result.remove(b)
            else:
                result.add(b)