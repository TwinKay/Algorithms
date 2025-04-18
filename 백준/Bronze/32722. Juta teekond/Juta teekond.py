import sys

a1 = int(sys.stdin.readline().strip())
a2 = int(sys.stdin.readline().strip())
a3 = int(sys.stdin.readline().strip())

if a1 in (1, 3) and a2 in (6, 8) and a3 in (2, 5):
    print("JAH")
else:
    print("EI")