'''
아이디어:
연산자 가능한 순열 만들기
+ 연산자 등장 횟수 arr를 통해 cnt 조절하면서 가능한 순열 만들기 
'''

import sys

def back_tracking(n,val):
    global min_val,max_val
    if n==N-1: # 연산자 N-1개(기저)
        min_val = min(min_val,val)
        max_val = max(max_val,val)
        return
    for i in range(4):
        if cnt_oper[i] != 0: # 연산자를 더 쓸 수 있을 때
            cnt_oper[i] -= 1
            if i == 0:
                back_tracking(n + 1, val+arr[n+1])
            elif i == 1:
                back_tracking(n + 1, val - arr[n + 1])
            elif i == 2:
                back_tracking(n + 1, val * arr[n + 1])
            else:
                back_tracking(n + 1, int(val / arr[n + 1])) # //연산 조심

            cnt_oper[i] += 1

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
cnt_oper = list(map(int, sys.stdin.readline().split()))

min_val = float('inf')
max_val = -float('inf')
back_tracking(0,arr[0])

print(max_val)
print(min_val)