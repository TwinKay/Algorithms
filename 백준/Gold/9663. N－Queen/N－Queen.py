'''
아이디어:
백트래킹을 통한 기본 N-Queen 문제
visited 3개 이용
'''
import sys

def n_queen(n):
    '''
    queen의 가능한 조합 수를 반환하는 함수
    :param n: (int) queen 수
    :return: None -> global로 정답 변수 접근
    '''
    global cnt
    if n==N:
        cnt += 1
        return
    for i in range(N):
        if visited1[i] == visited2[n-i] == visited3[n+i] == 0: # 공격할 수 없는 경우
            visited1[i] = visited2[n-i] = visited3[n+i] = 1
            n_queen(n+1)
            visited1[i] = visited2[n-i] = visited3[n+i] = 0


N = int(sys.stdin.readline())
visited1 = [0]*N
visited2 = [0]*2*N
visited3 = [0]*2*N

cnt = 0
n_queen(0)
print(cnt)