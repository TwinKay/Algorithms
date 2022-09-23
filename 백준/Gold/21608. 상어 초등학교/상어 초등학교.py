# 보기 쉽게 다시 수정할 것!

import sys

n = int(sys.stdin.readline())

def get_index(result, d):
    for id1, x in enumerate(result):
        for id2, y in enumerate(x):
            if y == d:
                return id1, id2
    return None

stu_num = []
total = dict()
for i in range(n**2):
    l = list(map(int, sys.stdin.readline().split()))
    stu_num.append(l[0])

    total[l[0]] = l[1:]

result = []
for _ in range(n):
    result.append([False]*n)

bin = []
for i in stu_num:
    love_num = []
    for _ in range(n):
        love_num.append([0]*n)

    for j in total[i]:
        if j in bin:
            ind = get_index(result, j)
            if ind != None:
                try:
                    love_num[ind[0]+1][ind[1]] += 1
                except IndexError:
                    pass
                try:
                    if ind[0] == 0:
                        pass
                    else:
                        love_num[ind[0]-1][ind[1]] += 1
                except IndexError:
                    pass
                try:
                    love_num[ind[0]][ind[1]+1] += 1
                except IndexError:
                    pass
                try:
                    if ind[1] == 0:
                        pass
                    else:
                        love_num[ind[0]][ind[1]-1] += 1
                except IndexError:
                    pass
    for e,q in enumerate(result):
        for r,w in enumerate(q):
            if w != False:
                love_num[e][r] = -1


    love_num_list = []
    for a in love_num:
        for b in a:
            love_num_list.append(b)
    m = max(love_num_list)
    if love_num_list.count(m) == 1:
        ind_2 = get_index(love_num, m)
        if result[ind_2[0]][ind_2[1]] == False:

            result[ind_2[0]][ind_2[1]] = i
            bin.append(i)

    else:
        try_list = []
        for x,c in enumerate(love_num):
            for y,d in enumerate(c):
                if d == m:
                    try_list.append((x,y))

        blank = [-1] * (n ** 2)
        for q in try_list:
            x = q[0] ; y = q[1]

            t = 0
            try:
                if result[x+1][y] == False:
                    t += 1
            except IndexError:
                pass
            try:
                if x == 0:
                    pass
                elif result[x-1][y] == False:
                    t += 1
            except IndexError:
                pass
            try:
                if result[x][y+1] == False:
                    t += 1
            except IndexError:
                pass
            try:
                if y == 0:
                    pass
                elif result[x][y-1] == False:
                    t += 1
            except IndexError:
                pass

            blank[x*n+y] = t

        m = max(blank)
        if blank.count(m) == 1:
            a = blank.index(m)
            ind1 = a//n ; ind2 = a%n

            if result[ind1][ind2] == False:
                result[ind1][ind2] = i
                bin.append(i)

        else:
            try_list = []
            for w, q in enumerate(blank):
                if q == m:
                    if result[w//n][w%n] == False:
                        result[w // n][w % n] = i
                        break

            bin.append(i)

sat = 0
for x,i in enumerate(result):
    for y,j in enumerate(i):
        t = 0
        try:
            if result[x+1][y] in total[j]:
                t += 1
        except:
            pass
        try:
            if x == 0:
                pass
            else:
                if result[x-1][y] in total[j]:
                    t += 1
        except:
            pass
        try:
            if result[x][y+1] in total[j]:
                t += 1
        except:
            pass
        try:
            if y == 0:
                pass
            else:
                if result[x][y-1] in total[j]:
                    t += 1
        except:
            pass

        if t == 0:
            sat += 0
        elif t == 1:
            sat += 1
        elif t == 2:
            sat += 10
        elif t == 3:
            sat += 100
        else:
            sat += 1000

print(sat)