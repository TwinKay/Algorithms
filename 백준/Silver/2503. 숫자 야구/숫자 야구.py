'''
아이디어:
브루트포스 + 단순 구현
'''
import sys

def is_valid(my_num, hint_info):
    '''
    질문에 적합한 수인지 반환하는 함수
    :param my_num: (int) 비교 대상
    :param hint_info: (list) 힌트 정보
    :return: (boolean) True: 적합한 수
    '''
    hint_num, strike, ball = hint_info
    cnt_total = 0
    cnt_strike = 0
    for i in range(3):
        if my_num[i] in hint_num:
            cnt_total += 1
            if my_num[i] == hint_num[i]:
                cnt_strike += 1

    if strike == cnt_strike and ball == cnt_total-cnt_strike:
        return True
    return False


N = int(sys.stdin.readline())
hints = []
for _ in range(N):
    a,b,c = sys.stdin.readline().split()
    hints.append([a,int(b),int(c)])

res_cnt = 0

for a in range(1,10):
    for b in range(1,10):
        for c in range(1,10):
            if a==b or b==c or a==c:
                continue
                
            num = str(a)+str(b)+str(c)
            flag = True
            for hint in hints:
                if not is_valid(num,hint):
                    flag = False
                    break
            if flag: # 모든 조건에 만족하면
                res_cnt += 1

print(res_cnt)