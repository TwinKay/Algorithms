import sys

A = int(sys.stdin.readline())
B = int(sys.stdin.readline())
C = int(sys.stdin.readline())
D = int(sys.stdin.readline())
E = int(sys.stdin.readline())

total_time = 0
if A < 0:
    total_time += (-A) * C
    total_time += D
    total_time += B * E
else:
    total_time += (B - A) * E

print(total_time)