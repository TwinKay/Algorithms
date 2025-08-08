'''
아이디어:
이진탐색 이용
mid**2가 target이 되는 순간 구하기
'''
import sys

def b_search(left,right,target):
    '''
    이진탐색 함수
    :param left: (int) left index
    :param right: (int) right index
    :return: (int) 제곱근
    '''
    while True:
        if left > right:
            return -1
        mid = (left+right)//2
        mid_val = mid*mid
        if mid_val == target:
            return mid
        elif mid_val > target:
            right = mid-1
        else:
            left = mid+1

N = int(sys.stdin.readline())
print(b_search(0,N,N))
