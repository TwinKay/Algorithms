'''
아이디어:
이전 추가된 수를 저장하며 비교하여 더 작을 때만 백트래킹
새로 만들어진 수는 num으로 *10을 통해 저장하며 나중에 정렬한 후에 index를 뽑아내기
'''
import sys

def back_tracking(before,num):
    '''
    감소하는 수를 만드는 함수
    :param before: (int) 이전에 저장된 수
    :param num: (int) 현재 만들어진 수
    :return: (None) -> res list에 추가함
    '''
    res.append(num)
    for i in range(10):
        if i < before:
            back_tracking(i,num*10+i)


N = int(sys.stdin.readline())
res = []
back_tracking(10,0)
res.sort()
if N > 1022:
    print(-1)
elif N == 0:
    print(0)
else:
    print(res[N+1])