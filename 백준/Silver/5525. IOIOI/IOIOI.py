# 풀이 참고해서 품!
import sys

n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
s = sys.stdin.readline().rstrip()

ans = 0
cursor = 0
cnt = 0

while cursor < m-1:
    if s[cursor:cursor+3] == 'IOI':
        cursor += 2
        cnt += 1
        if cnt == n:
            ans += 1
            cnt -= 1
    else:
        cursor += 1
        cnt = 0

print(ans)