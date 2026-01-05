t = int(input())

win = {
    ('R', 'S'),
    ('S', 'P'),
    ('P', 'R')
}

for _ in range(t):
    n = int(input())
    p1_score = 0
    p2_score = 0

    for _ in range(n):
        a, b = input().split()
        if a == b:
            continue
        elif (a, b) in win:
            p1_score += 1
        else:
            p2_score += 1

    if p1_score > p2_score:
        print("Player 1")
    elif p1_score < p2_score:
        print("Player 2")
    else:
        print("TIE")