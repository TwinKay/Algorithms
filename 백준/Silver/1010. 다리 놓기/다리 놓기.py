import sys
import math

T = int(sys.stdin.readline())
for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    result = math.factorial(M) // (math.factorial(N) * math.factorial(M - N))
    print(result)
