'''
python 정렬 기준: 숫자, 대문자, 소문자 및 짧은 순 -> 그대로 정렬 가능
'''

prt = []

import sys

N = 9
graph = []
for _ in range(N):
    graph.append(list(sys.stdin.readline().split()))

arr = [] # 3중 리스트, 정렬 기준: 중간 목표 후 세부 목표
for i in range(1,9,3):
    for j in range(1,9,3):
        # [j,i]: 중앙값
        if i==4 and j==4:
            continue
        temp_arr = [graph[i][j],[]]
        for k in range(-1,2):
            for l in range(-1,2):
                if k==0 and l==0:
                    continue
                temp_arr[1].append(graph[i+k][j+l])
        arr.append(temp_arr)

arr = sorted(arr, key=lambda x:x[0])
for i in range(8):
    detail_arr = arr[i]
    prt.append(f"#{i+1}. {detail_arr[0]}")
    detail_arr[1] = sorted(detail_arr[1])
    for j in range(8):
        prt.append(f'#{i+1}-{j+1}. {detail_arr[1][j]}')

print("\n".join(prt))
