import sys, math

p1, q1, p2, q2 = map(int, sys.stdin.readline().split())
N = p1 * p2
D = 2 * q1 * q2
g = math.gcd(N, D)
D //= g
print(1 if D == 1 else 0)