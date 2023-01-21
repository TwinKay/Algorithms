def solution(babbling):
    cnt = 0
    for i in babbling:
        check='first'
        while i:
            if i[0] =='a' and check != i[0:3]:
                check = i[0:3]
                if i[0:3] == 'aya':
                    i = i[3:]
                else:
                    break
            elif i[0] == 'y' and check != i[0:2]:
                check = i[0:2]
                if i[0:2] == 'ye':
                    i = i[2:]
                else:
                    break
            elif i[0] == 'w' and check != i[0:3]:
                check = i[0:3]
                if i[0:3] == 'woo':
                    i = i[3:]
                else:
                    break
            elif i[0] == 'm' and check != i[0:2]:
                check = i[0:2]
                if i[0:2] == 'ma':
                    i = i[2:]
            else:
                break
        if i =='':
            cnt += 1

    return cnt