import sys
while True:
    n = sys.stdin.readline().strip()

    if int(n) == 0:
        break
    else:
        if len(n)%2 == 0:
            a = n[:len(n)//2]
            b = n[len(n)//2:]

        else:
            a = n[:len(n) // 2]
            b = n[len(n) // 2+1:]

        if a == b[::-1]:
            print('yes')
        else:
            print('no')