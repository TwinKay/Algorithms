'''
아이디어:
이진 탐색 이용
최대 가능 예산과 현재 기준 필요 예산 비교를 기준으로 이분 탐색
'''
import sys

def get_deposit_info(limit):
    '''
    특정 상한선 기준에서 각 지방의 받는 예산 중 MAX, SUM을 반환하는 함수
    :param limit: (int) 상한선
    :return: (list(int)) 각 지방의 받는 예산 중 MAX, SUM
    '''
    max_val = 0
    for a in arr:
        if a < limit:
            max_val = max(max_val,a)
        else:
            max_val = max(max_val,limit)
    sum_val = 0
    for a in arr:
        sum_val += min(a,limit)

    return [max_val,sum_val]


def b_search(left,right):
    '''
    예산 안에서 지방이 받는 예산을 최대로 하도록 할 때의
    특정 지방의 받을 수 있는 최대액을 이진 탐색으로 구하는 함수
    :param left: (int) 더 작은 금액
    :param right: (int) 더 큰 금액
    :return: (int) 특정 지방의 받을 수 있는 최대액
    '''
    result = 0
    while left <= right:
        mid = (left+right)//2
        max_city_deposit, sum_total_deposit = get_deposit_info(mid)

        if sum_total_deposit <= MAX_DEPOSIT:
            result = max_city_deposit
            left = mid+1

        else:
            right = mid-1

    return result


N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
MAX_DEPOSIT = int(sys.stdin.readline())

print(b_search(0,MAX_DEPOSIT))