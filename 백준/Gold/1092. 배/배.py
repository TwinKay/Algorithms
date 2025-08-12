'''
아이디어:
greedy로 풀이
컨테니어를 무거운 순서대로 높은 성능의 크레인부터 옮기기
'''
import sys

N = int(sys.stdin.readline())
crains = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
boxes = list(map(int, sys.stdin.readline().split()))

crains.sort(reverse=True) #  내림차순
boxes.sort(reverse=True)


if crains[0] < boxes[0]: # 옮길 수 없는 박스가 있음
    print(-1)
else:
    time = 0
    while boxes: # 박스를 모두 옮긴 경우가 아니면
        time += 1
        remove_idxs = []
        box_start_idx= 0
        for crain in crains:
            for box_idx in range(box_start_idx,len(boxes)):
                if crain >= boxes[box_idx]:  # 옮길 수 있으면
                    remove_idxs.append(box_idx)
                    box_start_idx = box_idx + 1
                    break
                    
        for r_idx in remove_idxs[::-1]:# 낮은 순부터 pop하면 순서가 바뀌기 때문
            boxes.pop(r_idx)
    print(time)