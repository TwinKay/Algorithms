import sys
t = 1
while True:
    a = sys.stdin.readline().rstrip()
    if a == '0':
        break
    else:
        print('Case ',end='')
        print(str(t),end='')
        print(': Sorting... done!')
        t += 1
        