'''
아이디어:
상담을 한다면 해당 소요 시간만큼 day에 더한 후, 백트래킹
단, 상담을 안하고 그냥 하루를 지나칠 수도 있음
'''
import sys
sys.setrecursionlimit(10**5)

def back_tracking(day,cost):
    global max_val
    if day == N: # 기저1: 가능한 경우
        max_val = max(max_val, cost)
        return
    elif day > N: # 기저2: 불가능한 경우(퇴사 후)
        return
    back_tracking(day + day_arr[day], cost + cost_arr[day]) # 상담에 해당하는 day,cost 더해서 재귀
    back_tracking(day+1,cost) # 아무 상담도 안 한 날

N = int(sys.stdin.readline())
day_arr = [] # 상담 소요 시간 arr
cost_arr = [] # 상담 비용(수익) arr
for _ in range(N):
    d,c = map(int, sys.stdin.readline().split())
    day_arr.append(d)
    cost_arr.append(c)
    
max_val = 0 # dummy
back_tracking(0,0)

print(max_val)
