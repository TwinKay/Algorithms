# 애초에 정리를 할 필요가 없는 경우 가능
# 물고기가 0이 되는 경우 X -> N*N 배열로 관리 가능 -> 함수 재사용성 up
import sys

def is_valid(x, y):
    return 0 <= x < N and 0 <= y < N

def add_fish(arr):
    min_val = float('inf')
    min_idxs = []
    for i in range(N):
        if arr[N-1][i] < min_val:
            min_val = arr[N-1][i]
            min_idxs = [i]
        elif arr[N-1][i] == min_val:
            min_idxs.append(i)

    for min_idx in min_idxs:
        arr[N-1][min_idx] += 1

    return arr

def find_height_and_width(arr):
    is_first_find = False
    left = None; right = None
    for j in range(N):
        if arr[N-2][j]:
            if is_first_find:
                right = j
            else:
                is_first_find = True
                left = j
                right = j
    for i in range(N):
        if arr[N-i-1][left] == 0:
            height = i
            break
    else: # 일자로 맨 위까지 차는 경우
        height = N

    return left,right,height

def levitate90(arr):
    arr[N-1][0],arr[N-2][1] = arr[N-2][1],arr[N-1][0]

    while True:
        left, right, height = find_height_and_width(arr)
        width = right - left + 1

        if height > N - 1 - right:
            break
        temp_arr = []
        for _ in range(height):
            temp_arr.append([0]*width)

        for i in range(height):
            for j in range(width):
                temp_arr[i][j] = arr[N-height+i][left+j]
                arr[N - height + i][left + j] = 0

        for i in range(width):
            for j in range(height):
                arr[N-2-i][j+right+1] = temp_arr[height-1-j][width-1-i]

    return arr


def spread(arr):
    spread_arr = []
    for _ in range(N):
        spread_arr.append([0] * N)

    for i in range(N):
        for j in range(N):
            if not arr[i][j]:
                continue

            for k in range(4):
                dx = j + delta_x[k]
                dy = i + delta_y[k]
                if not is_valid(dx, dy):
                    continue
                if arr[dy][dx] == 0:
                    continue
                if arr[dy][dx] >= arr[i][j]:
                    continue
                val = int((arr[i][j] - arr[dy][dx]) / 5)
                spread_arr[i][j] -= val
                spread_arr[dy][dx] += val

    for i in range(N):
        for j in range(N):
            if spread_arr[i][j]:
                arr[i][j] += spread_arr[i][j]

    return arr

def flatten(arr):
    flat_graph = []
    for _ in range(N):
        flat_graph.append([0]*N)

    idx = 0
    for j in range(N):
        for i in range(N-1,-1,-1):
            if not arr[i][j]:
                break
            flat_graph[N-1][idx] = arr[i][j]
            idx += 1

    return flat_graph


def levitate180(arr):
    for j in range(N // 2):
        arr[N - 2][N - 1 - j] = arr[N - 1][j]
        arr[N - 1][j] = 0

    for i in range(2):
        for j in range(N // 4):
            arr[N - 3 - i][N - 1 - j] = arr[N - 2 + i][j + N // 2]
            arr[N - 2 + i][j + N // 2] = 0

    return arr


def is_end(arr):
    min_val = float('inf')
    max_val = -float('inf')
    for j in range(N):
        min_val = min(min_val, arr[N - 1][j])
        max_val = max(max_val, arr[N - 1][j])

    if max_val - min_val <= K:
        return True
    return False


delta_x = [0, 0, -1, 1]
delta_y = [1, -1, 0, 0]

N,K = map(int, sys.stdin.readline().split())
graph = []
for _ in range(N):
    graph.append([0]*N)
temp = list(map(int, sys.stdin.readline().split()))
for i in range(N):
    graph[N-1][i] = temp[i]

time = 0
while not is_end(graph):
    time += 1

    graph = add_fish(graph)
    graph = levitate90(graph)
    graph = spread(graph)
    graph = flatten(graph)
    graph = levitate180(graph)
    graph = spread(graph)
    graph = flatten(graph)

print(time)