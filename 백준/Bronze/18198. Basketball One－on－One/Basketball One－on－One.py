record = input().strip()

a_score = 0
b_score = 0

i = 0
while i < len(record):
    player = record[i]
    point = int(record[i+1])

    if player == 'A':
        a_score += point
    else:
        b_score += point

    if max(a_score, b_score) >= 11:
        if abs(a_score - b_score) >= 2:
            if a_score > b_score:
                print('A')
            else:
                print('B')
            break
    i += 2