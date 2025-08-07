'''
아이디어:
퀵 소트 구현
'''
import sys
sys.setrecursionlimit(10**5)

def quick_sort(arr, left, right):
    if left >= right: # left랑 right가 같아지면 return
        return

    pivot = arr[left]
    i = left + 1 # pivot 제외
    j = right

    while i <= j:
        while i <= right and arr[i] <= pivot:
            i += 1
        while j >= left + 1 and arr[j] >= pivot:
            j -= 1
        if i <= j:
            arr[i], arr[j] = arr[j], arr[i] # 값 바꿔주기

    arr[left], arr[j] = arr[j], arr[left] # pivot 넣기

    # 재귀
    quick_sort(arr, left, j - 1)
    quick_sort(arr, j + 1, right)

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
quick_sort(arr, 0, len(arr)-1)

for a in arr:
    print(a)