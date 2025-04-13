import sys

S = int(sys.stdin.readline())
M_a, F_ab, M_b = map(int, sys.stdin.readline().split())

time = M_a + F_ab + M_b

if time >= S or S <= 240:
    print("high speed rail")
else:
    print("flight")
