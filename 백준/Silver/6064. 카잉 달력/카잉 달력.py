# 풀이 참고,, 다시 풀어볼 것..!
import sys

t = int(sys.stdin.readline())

for _ in range(t):
    m,n,x,y = map(int, sys.stdin.readline().split())
    cnt = -1
    while x <= m*n:
        if (x-y) % n == 0:
            cnt = x
            break
        x += m
    print(cnt)