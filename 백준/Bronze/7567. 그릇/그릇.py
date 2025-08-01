'''
stack -1 체크하면서 길이 확인
'''
import sys

s = sys.stdin.readline().rstrip()

stack = []
res = 0
stack.append(s[0])
res += 10
for i in range(1,len(s)):
    if s[i] == stack[-1]:
        res += 5
        stack.append(s[i])
    else:
        res += 10
        stack.append(s[i])
print(res)
