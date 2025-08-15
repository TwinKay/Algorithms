'''
돌리는 부분을 모두 만들 필요가 있을까? -> 반대는 3번 돌리면 된다
확인은 전개도에서 빈공간도 그냥 체크해서 복잡하게 구현할 필요 X -> 시간 충분
'''
import sys

def is_same_color(x,y): # 해당 그룹이 모두 같은 색인지 여부
    main_color = cube[y][x]
    for i in range(2):
        for j in range(2):
            if cube[y+i][x+j] != main_color:
                return False

    return True


def check_made(): # 전개도에서 빈 공간 포함이지만, 간단히 구현
    for i in range(0,6,2):
        for j in range(0,8,2):
            if not is_same_color(j,i):
                return False
    return True


def turn_up(direct):
    for _ in range(direct):
        temp1 = cube[2][6]; temp2 = cube[2][7]
        cube[2][6],cube[2][7] = cube[2][4],cube[2][5]
        cube[2][4],cube[2][5] = cube[2][2],cube[2][3]
        cube[2][2],cube[2][3] = cube[2][0],cube[2][1]
        cube[2][0],cube[2][1] = temp1,temp2


def turn_down(direct): # 전개도를 상하반전 시키면 turn_up과 동일
    global cube
    temp = []
    for c in cube[::-1]:
        temp.append(c)
    cube = temp
    turn_up(direct)


def turn_front(direct):
    for _ in range(direct):
        temp1 = cube[1][2]; temp2 =cube[1][3]
        cube[1][2],cube[1][3] = cube[3][1],cube[2][1]
        cube[3][1], cube[2][1] = cube[4][2],cube[4][3]
        cube[4][2], cube[4][3] = cube[3][4],cube[2][4]
        cube[3][4], cube[2][4] = temp1,temp2


def turn_back(direct):
    for _ in range(direct):
        temp1 = cube[0][2]; temp2 = cube[0][3]
        cube[0][2],cube[1][3] = cube[2][0],cube[3][0]
        cube[2][0],cube[3][0] = cube[5][2],cube[5][3]
        cube[5][2],cube[5][3] = cube[3][5],cube[2][5]
        cube[3][5], cube[2][5] = temp1,temp2


def turn_right(direct):
    for _ in range(direct):
        temp1 = cube[0][3]; temp2 = cube[1][3]
        cube[0][3],cube[1][3] = cube[2][3],cube[3][3]
        cube[2][3], cube[3][3] = cube[4][3],cube[5][3]
        cube[4][3], cube[5][3] = cube[2][6],cube[3][6]
        cube[2][6], cube[3][6] = temp1,temp2


def turn_left(direct):
    for _ in range(direct):
        temp1 = cube[0][2]; temp2 = cube[1][2]
        cube[0][2],cube[1][2] = cube[2][2],cube[3][2]
        cube[2][2], cube[3][2] =cube[4][2],cube[5][2]
        cube[4][2], cube[5][2] = cube[2][7],cube[3][7]
        cube[2][7], cube[3][7] = temp1,temp2


# 입력
arr = list(map(int, sys.stdin.readline().split()))

cube_first = []
for _ in range(6):
    cube_first.append([0]*8)

num = 0
for i in range(6):
    for j in range(2,4):
        cube_first[i][j] = arr[num]
        num += 1

for i in range(2,4):
    for j in range(2):
        cube_first[i][j] = arr[num]
        num += 1
for i in range(2,4):
    for j in range(4,6):
        cube_first[i][j] = arr[num]
        num += 1
for i in range(2,4):
    for j in range(6,8):
        cube_first[i][j] = arr[num]
        num += 1


moves = [turn_up, turn_down, turn_front, turn_back, turn_right, turn_left] # 돌리는 함수들

is_made = False
for move in moves:
    for d in (1, 3): # 1번 돌리기, 3번 돌리기(=반대 방향)
        cube = [c[:] for c in cube_first]
        move(d)
        if check_made():
            is_made = True
            break
    if is_made:
        break

if is_made:
    print(1)
else:
    print(0)