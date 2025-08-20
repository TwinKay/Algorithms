import sys
from itertools import combinations

color_dic = {}
color_dic["CIRCLE"] = 0
color_dic["TRIANGLE"] = 1
color_dic["SQUARE"] = 2

color_dic["YELLOW"] = 0
color_dic["RED"] = 1
color_dic["BLUE"] = 2

color_dic["GRAY"] = 0
color_dic["WHITE"] = 1
color_dic["BLACK"] = 2

cards = []
for _ in range(9):
    a,b,c = sys.stdin.readline().split()
    a = color_dic[a]
    b = color_dic[b]
    c = color_dic[c]
    cards.append([a,b,c])

posies = set()
for comb in combinations(range(len(cards)),3):
    card1 = cards[comb[0]]
    card2 = cards[comb[1]]
    card3 = cards[comb[2]]
    set_arr = [set(),set(),set()]
    for i in range(3):
        set_arr[i].add(card1[i])
        set_arr[i].add(card2[i])
        set_arr[i].add(card3[i])
    for s in set_arr:
        if len(s) == 2:
            break
    else:
        posies.add(tuple(comb))

score = 0
is_get3 = False
Q = int(sys.stdin.readline())
for _ in range(Q):
    query = sys.stdin.readline().rstrip()

    if query == 'G':
        if is_get3:
            score -= 1
        else:
            if len(posies) == 0:
                score += 3
                is_get3 = True
            else:
                score -= 1
    else:
        trash,a,b,c = query.split()
        lst = [int(a)-1,int(b)-1,int(c)-1]
        lst.sort()
        tp = tuple(lst)
        if tp in posies:
            posies.remove(tp)
            score += 1
        else:
            score -= 1
print(score)