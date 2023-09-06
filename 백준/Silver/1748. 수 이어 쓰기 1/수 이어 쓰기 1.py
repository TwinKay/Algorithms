import sys

n = sys.stdin.readline().rstrip()
l_n = len(n)
n = int(n)

pre = 0
for i in range(1, l_n):
    pre += (9*10**(i-1)) * i

print(pre + (n-(10**(l_n-1))+1)*l_n)