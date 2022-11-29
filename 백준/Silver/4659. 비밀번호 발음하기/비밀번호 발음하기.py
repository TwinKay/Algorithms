import sys

con = ['b','c','d','f','g','h','j','k','l','m','n','p','q','r','s','t','v','w','x','y','z']
vo = ['a','e','i','o','u']

while True:
    s = sys.stdin.readline().rstrip()
    if s == 'end':
        break
    else:
        #1
        check_vo = False
        for i in vo:
            if i in s:
                check_vo = True
                break
        #2
        check_3 = True
        for i in range(len(s)-2):
            words = s[i:i+3]
            res = [0,0]
            for j in words:
                if j in con:
                    res[0] += 1
                elif j in vo:
                    res[1] += 1
            if res[0] == 3 or res[1] == 3:
                check_3 = False
                break

        #3
        check_2 = True
        for i in range(len(s)-1):
            if s[i] == 'e' and s[i+1] == 'e':
                pass
            elif s[i] == 'o' and s[i+1] == 'o':
                pass
            elif s[i] == s[i+1]:
                check_2 = False
                break

        if check_vo == True and check_3 == True and check_2 == True:
            print('<'+s+'>'+' is acceptable.')
        else:
            print('<'+s+'>'+' is not acceptable.')