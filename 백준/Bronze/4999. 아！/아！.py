import sys
s1 = sys.stdin.readline().rstrip()
s2 = sys.stdin.readline().rstrip()
if len(s1) >= len(s2):
    print('go')
else:
    print('no')