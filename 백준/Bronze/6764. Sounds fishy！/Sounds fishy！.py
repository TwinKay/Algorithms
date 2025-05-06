import sys

depths = [int(sys.stdin.readline()) for _ in range(4)]
a, b, c, d = depths

if a < b < c < d:
    print("Fish Rising")
elif a > b > c > d:
    print("Fish Diving")
elif a == b == c == d:
    print("Fish At Constant Depth")
else:
    print("No Fish")
