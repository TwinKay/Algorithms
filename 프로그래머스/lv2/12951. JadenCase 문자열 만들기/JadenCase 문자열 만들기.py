def solution(s):
    num = list(range(10))
    ans = ''
    check = False
    s = s.lower()
    for i in s:
        if i == ' ':
            ans += ' '
            check = False
        else:
            if check == True:
                ans += i
            else:
                check = True
                if i in num:
                    ans += i
                else:
                    ans += i.upper()

    return ans