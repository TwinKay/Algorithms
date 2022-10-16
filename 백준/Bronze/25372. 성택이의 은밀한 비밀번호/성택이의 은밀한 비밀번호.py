import sys

for _ in range(int(sys.stdin.readline())):
    s = sys.stdin.readline().rstrip()
    if 6<=len(s)<=9:
        print('yes')
    else:
        print('no')