import sys

s = set()

n = int(sys.stdin.readline())

for _ in range(n):
    a = sys.stdin.readline().rstrip()

    if a == 'all':
        s = set(range(1,21))
    elif a == 'empty':
        s = set()
    else:
        c, b = a.split()
        b = int(b)

        if c == 'add':
            s.add(b)
        elif c == 'remove':
            s.discard(b)
        elif c == 'check':
            if b in s:
                print(1)
            else:
                print(0)
        elif c == 'toggle':
            if b in s:
                s.discard(b)
            else:
                s.add(b)