import sys

TC = int(sys.stdin.readline())
for _ in range(TC):
    s = sys.stdin.readline().strip()
    ans = 0
    for i, c in enumerate(s):
        if c == 'D':
            ans = i
            break
    else:
        ans = len(s)
    print(ans)
