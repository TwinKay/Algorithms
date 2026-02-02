import sys

P, K = sys.stdin.readline().split()
K = int(K)

is_prime = [True] * K
is_prime[0] = is_prime[1] = False

for i in range(2, int(K ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, K, i):
            is_prime[j] = False

for i in range(2, K):
    if is_prime[i]:
        remainder = 0
        for ch in P:
            remainder = (remainder * 10 + int(ch)) % i
        if remainder == 0:
            print("BAD", i)
            sys.exit()

print("GOOD")