import sys

n = sys.stdin.readline().rstrip()
m = int(sys.stdin.readline())

buttons = list(map(str,range(10)))
if m != 0:
    broken = list(sys.stdin.readline().split())
    for i in broken:
        buttons.remove(i)

if m == 10:
    print(abs(int(n)-100))
    sys.exit(0)

# 윗 자리 수, 아래 자리 수, 같은 자리 수 모든 경우 만든 후, 오차 작은 것 (+- 둘 다 쓰는 경우는 없음)

l = len(n)
n = int(n)
total = [abs(100-n)]

#if 로 경우 다 나눠야하나...?
if l == 1:
    for i in buttons:
        total.append(abs(n-int(i))+1)

    if buttons[0] == '0':
        try:
            total.append(abs(n-int(buttons[1]+'0'))+2)
        except:
            pass
    else:
        total.append(abs(n-int(buttons[0]*2))+2)

elif l == 2:
    total.append(abs(n-int(buttons[-1]))+1)

    for i in buttons:
        for j in buttons:
            if i != '0':
                total.append(abs(n-int(i+j))+2)

    if buttons[0] == '0':
        try:
            total.append(abs(n-int(buttons[1]+'00'))+3)
        except:
            pass
    else:
        total.append(abs(n-int(buttons[0]*3))+3)

elif l == 3:
    total.append(abs(n-int(buttons[-1]*2))+2)

    for i in buttons:
        for j in buttons:
            for k in buttons:
                if i != '0':
                    total.append(abs(n-int(i+j+k))+3)

    if buttons[0] == '0':
        try:
            total.append(abs(n-int(buttons[1]+'000'))+4)
        except:
            pass
    else:
        total.append(abs(n-int(buttons[0]*4))+4)

elif l == 4:
    total.append(abs(n-int(buttons[-1]*3))+3)

    for i in buttons:
        for j in buttons:
            for k in buttons:
                for a in buttons:
                    if i != '0':
                        total.append(abs(n-int(i+j+k+a))+4)

    if buttons[0] == '0':
        try:
            total.append(abs(n-int(buttons[1]+'0000'))+5)
        except:
            pass
    else:
        total.append(abs(n-int(buttons[0]*5))+5)

elif l == 5:
    total.append(abs(n-int(buttons[-1]*4))+4)

    for i in buttons:
        for j in buttons:
            for k in buttons:
                for a in buttons:
                    for b in buttons:
                        if i != '0':
                            total.append(abs(n-int(i+j+k+a+b))+5)

    if buttons[0] == '0':
        try:
            total.append(abs(n-int(buttons[1]+'00000'))+6)
        except:
            pass
    else:
        total.append(abs(n-int(buttons[0]*6))+6)

elif l == 6:
    total.append(abs(n-int(buttons[-1]*5))+5)

    for i in buttons:
        for j in buttons:
            for k in buttons:
                for a in buttons:
                    for b in buttons:
                        for c in buttons:
                            if i != '0':
                                total.append(abs(n-int(i+j+k+a+b+c))+6)

    if buttons[0] == '0':
        try:
            total.append(abs(n-int(buttons[1]+'000000'))+7)
        except:
            pass
    else:
        total.append(abs(int(buttons[0]*7))+7)

print(min(total))