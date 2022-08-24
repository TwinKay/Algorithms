import sys

n = int(sys.stdin.readline())
main = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
case = list(map(int, sys.stdin.readline().split()))
main.sort()

def binary(main_list, case_i):
    start = 0 ; end = n-1
    while start <= end:
        mid = (start+end)//2
        if main_list[mid] == case_i:
            return 1
        elif main_list[mid] > case_i:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for i in range(m):
    if binary(main, case[i]) == 1:
        print(1, end=' ')
    else:
        print(0, end=' ')