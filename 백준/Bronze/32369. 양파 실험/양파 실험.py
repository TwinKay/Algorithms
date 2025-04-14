import sys

N, A, B = map(int, sys.stdin.readline().split())

praise = 1
insult = 1

for _ in range(N):
    praise += A
    insult += B

    if praise == insult:
        insult -= 1
    elif insult > praise:
        praise, insult = insult, praise

print(praise, insult)
