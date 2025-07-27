'''
아이디어:
cnt_arr를 통한 시간 줄이기
'''

import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

l,r = 0,0
cnt_arr = [0]*10 # 과일 종류별 개수를 저장할 배열 (idx 0은 dummy)
# 과일 1개 넣고 시작
cnt_arr[arr[0]] += 1
cnt_type = 1
max_len = 1

while r < N-1:
    # 현재 과일 종류가 1개일 경우 -> 무조건 확장 가능
    if cnt_type == 1:
        r += 1
        # 새로운 종류 추가
        if cnt_arr[arr[r]] == 0:
            cnt_arr[arr[r]] += 1
            cnt_type += 1
        # 기존 포함된 종류
        else:
            cnt_arr[arr[r]] += 1
    # 현재 과일 종류가 2개일 경우
    else:
        # 다음 과일이 현재 종류 중 하나일 경우 -> 확장 가능
        if r + 1 < N and cnt_arr[arr[r+1]] != 0:
            r += 1
            cnt_arr[arr[r]] += 1
        else:
            # 현재 한 종류
            if r + 1 < N and cnt_type == 1:
                r += 1
                cnt_arr[arr[r]] += 1
                cnt_type += 1
            # 현재 두 종류
            else:
                cnt_arr[arr[l]] -= 1
                # 제외 시 종류가 사라지면
                if cnt_arr[arr[l]] == 0:
                    cnt_type -= 1
                l += 1

    max_len = max(max_len, r - l + 1)

print(max_len)