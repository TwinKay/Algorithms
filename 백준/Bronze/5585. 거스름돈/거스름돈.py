import sys

n = int(sys.stdin.readline())
n = 1000-n

cnt = 0
for _ in range(n//500):
    n -= 500
    cnt += 1

for _ in range(n//100):
    n -= 100
    cnt += 1

for _ in range(n//50):
    n -= 50
    cnt += 1

for _ in range(n//10):
    n -= 10
    cnt += 1

for _ in range(n//5):
    n -= 5
    cnt += 1

for _ in range(n//1):
    n -= 1
    cnt += 1

print(cnt)