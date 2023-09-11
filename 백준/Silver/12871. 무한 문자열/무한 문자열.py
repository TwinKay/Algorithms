import sys

s_1 = sys.stdin.readline().rstrip()
s_2 = sys.stdin.readline().rstrip()

long_s_1 = s_1*len(s_2)
long_s_2 = s_2*len(s_1)

if long_s_1 == long_s_2:
    print(1)
else:
    print(0)