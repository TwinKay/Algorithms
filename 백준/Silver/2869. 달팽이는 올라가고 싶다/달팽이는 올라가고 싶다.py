a, b, c = map(int, input().split())
if (c-b) % (a-b) == 0:
    print((c-b)//(a-b))
else:
    print((c-b)//(a-b)+1)