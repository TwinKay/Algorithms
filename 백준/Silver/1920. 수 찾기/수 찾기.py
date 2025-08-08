'''
아이디어:
이진탐색 이용
주의: 정렬 안 된 arr 입력
'''
def b_search(left,right,target):
    '''
    이진탐색 함수
    :param left: (int) left index
    :param right: (int) right index
    :return: (int) 값이 있으면 1
    '''
    while True:
        if left > right:
            return 0
        mid = (left+right)//2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            right = mid-1
        else:
            left = mid+1

N = int(input())
arr = list(map(int, input().split()))
arr.sort() # 이진탐색에서는 정렬 필수

Q = int(input())
queries = list(map(int, input().split()))
for query in queries:
    print(b_search(0,N-1,query))

