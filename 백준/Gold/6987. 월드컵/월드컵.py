'''
아이디어:
백트래킹 -> 매치 조합들을 통한 백트래킹 및 보드에서 감소시키기

풀이시간: ~20:22
실행시간:
메모리:
시도 횟수:
'''
import sys

def back_track(idx, board):
    if idx == len(matches):
        for i in range(6):
            for j in range(3):
                if board[i][j] != 0:
                    return False
        return True

    a,b = matches[idx]

    if board[a][0] > 0 and board[b][2] > 0:
        board[a][0] -= 1
        board[b][2] -= 1
        if back_track(idx+1, board):
            return True
        board[a][0] += 1
        board[b][2] += 1

    if board[a][1] > 0 and board[b][1] > 0:
        board[a][1] -= 1
        board[b][1] -= 1
        if back_track(idx+1, board):
            return True
        board[a][1] += 1
        board[b][1] += 1

    if board[a][2] > 0 and board[b][0] > 0:
        board[a][2] -= 1
        board[b][0] -= 1
        if back_track(idx+1, board):
            return True
        board[a][2] += 1
        board[b][0] += 1

    return False

# 가능한 매치 조합 미리 뽑기
matches = []
for i in range(6):
    for j in range(i+1,6):
        matches.append((i,j))

res = []
for t in range(4):
    results = list(map(int, sys.stdin.readline().split()))

    if sum(results) != 30: # 절대 불가능한 경우
        res.append(0)
        continue

    board = []
    for i in range(6):
        board.append([])
        for j in range(3):
            board[i].append(results[i*3+j])

    if back_track(0,board):
        res.append(1)
    else:
        res.append(0)

print(*res)
