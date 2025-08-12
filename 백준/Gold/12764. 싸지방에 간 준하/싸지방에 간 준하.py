'''
아이디어:
시작 시간을 +num, 종료 시간을 -num로 이용하는 arr 생성 후, 각 상황에 맞게 pq에 컴퓨터 번호 넣거나 빼기
'''
import sys
from heapq import heappush,heappop,heapify

N = int(sys.stdin.readline())
time_arr = [0]*1_000_001 # 최대 시간
for i in range(1,N+1):
    info = list(map(int, sys.stdin.readline().split()))
    time_arr[info[0]] += i # 시작, i는 사람의 idx를 기억하기 위함
    time_arr[info[1]] -= i # 종료

pq = list(range(1,100_001)) # 가능한 컴퓨터 수
heapify(pq)
used_cnt_arr = [0]*100_001 # 컴퓨터 번호(idx) 별 사용한 횟수를 기록하는 arr
save_arr = [0]*100_001 # 사람 번호(idx)에 이용 중인 컴퓨터 번호를 임시 저장하는 arr
for person_num in time_arr:
    if person_num == 0: # 없어도 되지만 실행 속도 개선 -> 먼저 처리
        continue
    elif person_num > 0: # 시작
        computer_num = heappop(pq) # 사용 가능한 가장 빠른 컴퓨터 번호
        used_cnt_arr[computer_num] += 1 # 해당 컴퓨터 사용 횟수 ++
        save_arr[person_num] = computer_num # 사람 idx에 사용중인 컴퓨터 번호 저장

    elif person_num < 0: # 종료
        computer_num = save_arr[-person_num] # 저장해놓은 컴퓨터 번호 다시 가져오기, 이후 0으로 바꿀 필요 X -> 자동 초기화된다.
        heappush(pq,computer_num) # 사용 완료한 컴퓨터 번호 다시 pq에 저장

res = []
for i in range(1,100_001):
    if used_cnt_arr[i] > 0: # 이용 기록이 있는 컴퓨터까지
        res.append(used_cnt_arr[i])
    else:
        break

print(len(res))
print(*res)