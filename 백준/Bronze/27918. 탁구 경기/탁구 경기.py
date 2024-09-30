import sys

n = int(sys.stdin.readline())
d = 0
p = 0
for i in range(n):
    s = sys.stdin.readline().rstrip()
    if (s == "D"):
        d += 1
    else:
        p += 1
    if (abs(d-p)>=2):
        break

print(d, end="")
print(":", end="")
print(p)