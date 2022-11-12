import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())
f = int(sys.stdin.readline())
l_1 = [a,b,c,d]
l_2 = [e,f]
l_1.sort(reverse=True)
print(sum(l_1[0:3])+max(l_2))