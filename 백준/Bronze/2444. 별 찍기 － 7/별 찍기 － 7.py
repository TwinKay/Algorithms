import sys

n = int(sys.stdin.readline())

for i in range(n):
    print(' '*(n-i-1), end='')
    print('*'*(2*i+1))

for i in range(n):
    print(' '*(i+1), end='')
    print('*'*((2*(n-i-1))-1))