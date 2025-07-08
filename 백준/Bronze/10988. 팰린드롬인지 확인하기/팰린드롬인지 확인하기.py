import sys

s = sys.stdin.readline().rstrip()
res = True
for i in range(len(s)):
    if s[i] != s[len(s)-1-i]:
        res = False
        break
    
if res:
    print(1)
else:
    print(0)