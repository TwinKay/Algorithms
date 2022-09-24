import sys

L = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

t = 0
for j,i in enumerate(s):
    t += (ord(i)-96)*31**j

print(t % 1234567891)