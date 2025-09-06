'''
더 효율적인 자료 구조나 직관적인 방법으로 시간날 때 다시 풀어보면 좋은 문제

[개요]
문제명: 새로운 게임 2
풀이 시간: 73분 30초
시도 횟수: 1회
실행 시간: 164ms
메모리: 112560KB
시간복잡도: 1000*10*10

[아이디어]
시뮬레이션

[타임라인]
구상: 18분
구현 (+ 단위 디버깅): 55분 30초
디버깅: 29분 30초

[구상]
(GOOD)
지금까지 가장 많은 시간인 18분을 구상에 투자한 것 같다.
실수할만한 조건들(빨강 뒤집기->이동한 것만, 파랑 2번 연속일 때 2번째는 direct update X등)을
확실하게 넘어갔다.

(BAD)
자료구조는 dict만 생각했다가 index를 말 번호로 사용하는 list도 구현 중간에 추가했다.
문제를 읽는 능력은 올라갔으나 이제 이런 부분도 챙겨보자!

[구현 + 단위 디버깅]
(GOOD)
구상에서 적어놓은 조건들을 잘 구현했다.

(BAD)
init direction의 arr를 잘못 적었거나 2중 반복문의 no flag break이나 얕은 복사처럼
사소한 실수가 많아서 시간이 오래 걸렸다. 구현을 할 때 좀 더 집중할 필요가 있어보인다.

[디버깅]
(GOOD)
약 30분이 걸리긴 했지만 turn,id 별로 잘 print하여 잘못된 부분을 쉽게 발견할 수 있었다.

[검증]
(GOOD)
구상할 때 양쪽이 파란색이면 제자리에서 턴마다 direction만 바뀌는 것이 엣지라고 종이에 적어놓고
다 풀고 해당 케이스를 검증한 후 제출했다.

[후기]
시간이 오래 걸려도 문제를 잘 읽는 건 정말 중요한 것 같다. 하지만 이제 구현에도 정신 꽉 잡고 짜자!

[개선사항]
중복된 코드들이 너무 많고 함수화도 필요해보인다
'''
import sys

def print_horses():
    for key in horses.keys():
        if horses[key]:
            print(f'{key}: {horses[key]}')

def init_direction(direct):
    arr = [None,3,1,0,2]
    return arr[direct]

delta_x = [0,-1,0,1]
delta_y = [-1,0,1,0]

N,K = map(int, sys.stdin.readline().split())
graph = []
graph.append([2]*(N+2))
for _ in range(N):
    graph.append([2]+list(map(int, sys.stdin.readline().split()))+[2])
graph.append([2]*(N+2))
N += 2

horses = {} # x,y -> [말 번호...]
for i in range(1,N+1):
    for j in range(1,N+1):
        horses[(j,i)] = []

horse_infos = [] # index가 말 번호 -> 항상 같이 업데이트
for k in range(K):
    y,x,direct = map(int, sys.stdin.readline().split())
    horses[(x,y)].append(k) # 말 번호(0부터)
    horse_infos.append([x,y,init_direction(direct)])

is_end = False
turn_cnt = 0
while True:
    if is_end: break
    turn_cnt += 1
    if turn_cnt == 1001:
        break

    # 여기에 반복문 넣어
    for horse_id in range(K):
        horse_x,horse_y,horse_direct = horse_infos[horse_id]
        horse_dx = horse_x + delta_x[horse_direct%4]
        horse_dy = horse_y + delta_y[horse_direct%4]
        if graph[horse_dy][horse_dx] == 2: # 범위 밖, 파랑
            horse_direct = (horse_direct+2)%4
            horse_infos[horse_id][2] = horse_direct
            horse_dx = horse_x + delta_x[horse_direct % 4]
            horse_dy = horse_y + delta_y[horse_direct % 4]
            if graph[horse_dy][horse_dx] == 2: # 여전히 이동 x
                continue
            elif graph[horse_dy][horse_dx] == 0: # 흰색
                same_group = horses[(horse_x, horse_y)]
                horse_idx_in_group = same_group.index(horse_id)
                move_ids, horses[(horse_x, horse_y)] = same_group[horse_idx_in_group:], same_group[:horse_idx_in_group]
                horses[(horse_dx, horse_dy)].extend(move_ids)

                for move_id in move_ids:
                    horse_infos[move_id] = [horse_dx, horse_dy, horse_infos[move_id][2]]

                if len(horses[(horse_dx, horse_dy)]) >= 4:
                    is_end = True
                    break
            else: # 빨강
                same_group = horses[(horse_x, horse_y)]
                horse_idx_in_group = same_group.index(horse_id)
                move_ids, horses[(horse_x, horse_y)] = same_group[horse_idx_in_group:], same_group[:horse_idx_in_group]
                horses[(horse_dx, horse_dy)].extend(move_ids[::-1])

                for move_id in move_ids:
                    horse_infos[move_id] = [horse_dx, horse_dy, horse_infos[move_id][2]]

                if len(horses[(horse_dx, horse_dy)]) >= 4:
                    is_end = True
                    break

        elif graph[horse_dy][horse_dx] == 0:
            same_group = horses[(horse_x,horse_y)]
            horse_idx_in_group = same_group.index(horse_id)
            move_ids, horses[(horse_x,horse_y)] = same_group[horse_idx_in_group:],same_group[:horse_idx_in_group]
            horses[(horse_dx,horse_dy)].extend(move_ids)

            for move_id in move_ids:
                horse_infos[move_id] = [horse_dx,horse_dy,horse_infos[move_id][2]]

            if len(horses[(horse_dx, horse_dy)]) >= 4:
                is_end = True
                break

        else: # 빨강
            same_group = horses[(horse_x,horse_y)]
            horse_idx_in_group = same_group.index(horse_id)
            move_ids, horses[(horse_x,horse_y)] = same_group[horse_idx_in_group:],same_group[:horse_idx_in_group]

            horses[(horse_dx,horse_dy)].extend(move_ids[::-1])
            for move_id in move_ids:
                horse_infos[move_id] = [horse_dx,horse_dy,horse_infos[move_id][2]]

            if len(horses[(horse_dx, horse_dy)]) >= 4:
                is_end = True
                break

if turn_cnt == 1001:
    print(-1)
else:
    print(turn_cnt)