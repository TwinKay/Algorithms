import sys
import math

n,k = map(int, sys.stdin.readline().split())

a = math.factorial(n) // ((math.factorial(k)*math.factorial(n-k)))

print(a%10007)