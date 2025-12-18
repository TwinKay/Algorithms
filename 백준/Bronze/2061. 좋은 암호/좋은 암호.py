import sys

K, L = sys.stdin.readline().split()
K = int(K)
L = int(L)

for i in range(2, L):
    if K % i == 0:
        print("BAD", i)
        sys.exit(0)

print("GOOD")