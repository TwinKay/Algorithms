import sys

s = int(sys.stdin.readline())

cnt = 0
i = 1
while True:
    if cnt > s:
        print(i-2)
        break
    elif cnt == s:
        print(i-1)
        break
    else:
        cnt += i
        i += 1