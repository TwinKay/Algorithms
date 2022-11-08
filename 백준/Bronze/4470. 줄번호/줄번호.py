import sys

for i in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    print(str(i+1), end='')
    print('. ', end = '')
    print(s)