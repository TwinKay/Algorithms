import sys

N = int(sys.stdin.readline().strip())
S = sys.stdin.readline().strip()

for i in range(1, N):
    if S[i] == 'J':
        print(S[i-1])