# 신발끈 공식 사용

import sys

n = int(sys.stdin.readline())

dots = []
for _ in range(n):
    x,y = map(int, sys.stdin.readline().split())
    dots.append([x,y])
    
# 반시계 방향 정렬? -> 정렬되어서 주어지넹..

ans = 0
for i in range(n-1):
    ans += dots[i][0] * dots[i+1][1]
ans += dots[-1][0] * dots[0][1]

for i in range(n-1):
    ans -= dots[i+1][0] * dots[i][1]
ans -= dots[0][0] * dots[-1][1]

ans /= 2
ans = abs(ans)
print(round(ans,2))