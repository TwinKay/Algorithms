# 코드가 너무 별로다.. 나중에 다시 풀 것!

import sys

s = sys.stdin.readline().strip()
s = s.split('>')

for i in s:
    if i == '':
        pass
    elif i[0] == '<':
        print(i+'>', end='')
    else:
        try:
            a,b = i.split('<')
            a = a.split()

            for l, k in enumerate(a):
                if l == len(a)-1:
                    k = k[::-1]
                    print(k, end = '')
                else:
                    k = k[::-1]
                    print(k, end = ' ')

            print('<'+b+'>', end = '')
        except:
            a = i
            a = a.split()

            for l, k in enumerate(a):
                if l == len(a)-1:
                    k = k[::-1]
                    print(k, end = '')
                else:
                    k = k[::-1]
                    print(k, end = ' ')