'''
아이디어:
greedy로 풀이
종료 시간이 빠르고 시작 시간이 빠른 순으로 정렬 후, greedy로 풀이
'''

N = int(input())
times = []
for _ in range(N):
    times.append(list(map(int, input().split())))

times.sort(key=lambda x:(x[1],x[0])) # 종료 시간이 빠르고 시작 시간이 빠른 순
cur_end_time = -1 # 0시 이후임으로 -1로 dummy
cnt = 0
for time in times:
    if time[0] >= cur_end_time: # 시간 배정이 가능한 경우
        cur_end_time = time[1]
        cnt += 1

print(cnt)