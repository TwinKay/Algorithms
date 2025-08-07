'''
아이디어:
막대기의 num을 1,2,3으로 하고 6-num1-num2를 통해
출발,도착 막대기가 아닌 곳에 넣어둔 후 움직이기
'''
import sys

def recu(n, a, b):
    if n == 1:
        prt.append(f'{a} {b}')

    else:
        recu(n-1, a, 6-a-b)
        prt.append(f'{a} {b}')
        recu(n-1, 6-a-b, b)

n = int(sys.stdin.readline())

prt = []
prt.append(str(2**n-1)) # 재귀 호출 cnt 필요없이 항상 하노이탑의 최소 이동 횟수
recu(n, 1, 3)
print("\n".join(prt))
