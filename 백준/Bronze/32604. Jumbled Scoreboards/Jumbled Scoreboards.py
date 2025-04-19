import sys

n = int(sys.stdin.readline())
prev_a, prev_b = 0, 0
flag = False
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())
    if a < prev_a or b < prev_b:
        print("no")
        flag = True
        break
    prev_a, prev_b = a, b
if flag == False:
    print("yes")

