def solution(s):
    cnt_c = 0
    cnt_chn = 0
    while True:
        if s == '1':
            break
        else:
            c = s.count('0')
            s = s.replace('0','')
            s = bin(len(s))[2:]
            cnt_c += c
            cnt_chn += 1

    answer = [cnt_chn,cnt_c]
    return answer