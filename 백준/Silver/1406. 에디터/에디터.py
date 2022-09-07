# 5397번 키로거랑 유사한 문제
# 직관적으로 데크로 풀 수 있으나, 리스트로 풀어보기!

import sys

s = sys.stdin.readline().rstrip()
n = int(sys.stdin.readline())
left_list = list(s)
right_list = []

for _ in range(n):
    a = sys.stdin.readline().rstrip()
    if a[0] == 'P':
        a,b = a.split()

        left_list.append(b)

    elif a == 'L':
        if left_list:
            right_list.append(left_list.pop())

    elif a == 'D':
        if right_list:
            left_list.append(right_list.pop())

    else:
        if left_list:
            left_list.pop()

print(''.join(left_list) + ''.join(right_list[::-1]))