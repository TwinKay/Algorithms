'''
전위 순회, 중위 순회, 후회 순회 풀이
=> 숫자로 바꿔서 쉽게 푼 뒤에 변환
'''

def alpa_to_num(alpa):
    return ord(alpa)-64

def num_to_alpa(num):
    return chr(num+64)

def pre_order(n):
    pre_order_arr.append(n)
    if left_child[n]:
        pre_order(left_child[n])
    if right_child[n]:
        pre_order(right_child[n])

def in_order(n):
    if left_child[n]:
        in_order(left_child[n])
    in_order_arr.append(n)
    if right_child[n]:
        in_order(right_child[n])

def post_order(n):
    if left_child[n]:
        post_order(left_child[n])
    if right_child[n]:
        post_order(right_child[n])
    post_order_arr.append(n)

import sys
sys.setrecursionlimit(10**5)

N = int(sys.stdin.readline())
left_child = [0]*(N+1)
right_child = [0]*(N+1)
for _ in range(N):
    a,b,c = sys.stdin.readline().split()
    a = alpa_to_num(a)
    if b != '.':
        b = alpa_to_num(b)
        left_child[a] = b
    if c != '.':
        c = alpa_to_num(c)
        right_child[a] = c

pre_order_arr = []
pre_order(1)
in_order_arr = []
in_order(1)
post_order_arr = []
post_order(1)
print("".join(list(map(num_to_alpa, pre_order_arr))))
print("".join(list(map(num_to_alpa, in_order_arr))))
print("".join(list(map(num_to_alpa, post_order_arr))))