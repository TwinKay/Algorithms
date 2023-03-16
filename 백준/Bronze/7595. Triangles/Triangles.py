import sys

while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    else:
        for i in range(n):
            print('*'*(i+1))