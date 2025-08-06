'''
아이디어:
한 팀에 가능한 조합(N//2명) 만든 후,
능력치 비교하기
'''

import sys

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(list(map(int, sys.stdin.readline().split())))

def back_tracking(n,start,team1):
    global min_val
    if n == half_N: # 기저 조건
        team2 = [] # 다른 팀 조합 만들기
        for i in range(N):
            if i not in team1:
                team2.append(i)
                
        team1_overall = 0
        for i in range(half_N): # i==j는 0이라 괜찮다 -> 조건 추가가 시간 더 들듯
            for j in range(half_N):
                team1_overall += arr[team1[i]][team1[j]]
        team2_overall = 0
        for i in range(half_N):
            for j in range(half_N):
                team2_overall += arr[team2[i]][team2[j]]
        min_val = min(min_val,abs(team1_overall-team2_overall))
        return

    for i in range(start,N):
        back_tracking(n+1,i+1,team1+[i])

half_N = N//2
min_val = float('inf')
back_tracking(0,0,[])
print(min_val)