'''
아이디어:
머지 소트 구현
'''
import sys

def merge_sort(arr, left, right):
    if left >= right: # 최대한 쪼개기
        return

    center = (left + right) // 2
    merge_sort(arr, left, center)
    merge_sort(arr, center + 1, right)

    temp = [] # 병합할 배열
    i = left
    j = center + 1

    while i <= center and j <= right:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1
        else:
            temp.append(arr[j])
            j += 1

    while i <= center:
        temp.append(arr[i])
        i += 1

    while j <= right:
        temp.append(arr[j])
        j += 1

    for k in range(len(temp)): # 병합 배열를 원래 배열에 반영
        arr[left + k] = temp[k]

N = int(sys.stdin.readline())
arr = []
for _ in range(N):
    arr.append(int(sys.stdin.readline()))
merge_sort(arr, 0, len(arr)-1)

for a in arr:
    print(a)