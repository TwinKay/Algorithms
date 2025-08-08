'''
아이디어:
이진탐색 이용
답은 원하는 길이와 같지 않을 수 있음(초과)
'''
import sys

def get_tree_length(height):
    '''
    특정 높이에서 나무를 잘랐을 때 얻는 나무 길이를 반환하는 함수
    :param (int) height: 절단기의 높이
    :return: (int) 얻은 나무 길이
    '''
    total_length = 0
    for a in arr:
        total_length += max(0,a-height)

    return total_length


def b_search(left,right,target_length):
    '''
    이진탐색 함수
    :param left: (int) left index (최소 높이)
    :param right: (int) right index (최대 높이)
    :param target_length: (int) 필요한 나무 길이
    :return: (int) 나무를 절단하는데 필요한 최대 높이
    '''
    result = 0
    while left <= right:
        mid = (left+right)//2
        tree_length = get_tree_length(mid)

        if tree_length >= target_length:
            result = mid
            left = mid+1
        else:
            right = mid-1
    return result


N,M = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
print(b_search(0,max(arr),M)) # max(arr)부터 탐색 가능