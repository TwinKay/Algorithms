import sys
import math

for _ in range(int(sys.stdin.readline())):
    a,b = map(int, sys.stdin.readline().split())

    print(math.factorial(b) // (math.factorial(a) * math.factorial(b - a)))