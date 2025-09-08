import sys

move_arr = list(map(int, sys.stdin.readline().split()))

dic_normal = {}
for i in range(0,39,2):
    dic_normal[i] = i+2
dic_normal[40] = -1

dic_special = {}
for i in range(13,17,3):
    dic_special[i] = i+3
dic_special[19] = 25
dic_special[22] = 24
dic_special[24] = 25
dic_special[28]=27
dic_special[27]=26
dic_special[26]=25
dic_special[25] = 30
dic_special[30] = 35
dic_special[35] = 40
dic_special[40] = -1


def find_destination(idx,is_special,move_num):
    if is_special:
        for _ in range(move_num):
            idx = dic_special[idx]
            if idx == -1:
                break
    else:
        for _ in range(move_num):
            idx = dic_normal[idx]
            if idx == -1:
                break

    return idx


def back_track(n,def_horse_idxs,def_horses_special,score):
    global res_max
    if n==10:
        res_max = max(res_max,score)
        return

    if (10-n)*40 + score <= res_max: # 가지 치기 강사님 코드 참고
        return

    for horse_id in range(4):
        is_cant_id = False
        horse_idxs = def_horse_idxs[:]
        horses_special = def_horses_special[:]

        horse_idx = horse_idxs[horse_id]
        if horse_idx == -1:
            continue
        move_num = move_arr[n]

        if horses_special[horse_id]:  # 30 중복 중 이미 안이면 여기서 처리
            dest = find_destination(horse_idx, 1, move_num)
            for j in range(4):
                if j == horse_id:
                    continue
                if horse_idxs[j] == -1:
                    continue
                if dest == horse_idxs[j] and horses_special[j]:
                    is_cant_id = True
                    break
                if dest == 40 and 40 in horse_idxs: # 40은 따로 처리해야함. special normal 둘다 포함
                    is_cant_id = True
                    break
            if is_cant_id:
                continue

            horse_idxs[horse_id] = dest
            if dest != -1:
                back_track(n+1,horse_idxs,horses_special,score+dest)
            else:
                back_track(n+1, horse_idxs, horses_special, score)


        else:
            if horse_idx in [10, 20, 30]:  # 10,20,30 따로 처리해서 하나만 보내야함
                # 이제 특별 라인
                horses_special[horse_id] = 1
                if horse_idx == 10:
                    dest = find_destination(13, 1, move_num - 1)
                    for j in range(4):
                        if j == horse_id:
                            continue
                        if horse_idxs[j] == -1:
                            continue
                        if dest == horse_idxs[j] and horses_special[j]:
                            is_cant_id = True
                            break
                        if dest == 40 and 40 in horse_idxs:  # 40은 따로 처리해야함. special normal 둘다 포함
                            is_cant_id = True
                            break
                    if is_cant_id:
                        continue

                    horse_idxs[horse_id] = dest
                    if dest != -1:
                        back_track(n+1,horse_idxs,horses_special,score+dest)
                    else:
                        back_track(n + 1, horse_idxs, horses_special, score)


                elif horse_idx == 20:
                    dest = find_destination(22, 1, move_num - 1)
                    for j in range(4):
                        if j == horse_id:
                            continue
                        if horse_idxs[j] == -1:
                            continue
                        if dest == horse_idxs[j] and horses_special[j]:
                            is_cant_id = True
                            break
                        if dest == 40 and 40 in horse_idxs:  # 40은 따로 처리해야함. special normal 둘다 포함
                            is_cant_id = True
                            break
                    if is_cant_id:
                        continue

                    horse_idxs[horse_id] = dest
                    if dest != -1:
                        back_track(n+1,horse_idxs,horses_special,score+dest)
                    else:
                        back_track(n + 1, horse_idxs, horses_special, score)

                else:
                    dest = find_destination(28, 1, move_num - 1)
                    for j in range(4):
                        if j == horse_id:
                            continue
                        if horse_idxs[j] == -1:
                            continue
                        if dest == horse_idxs[j] and horses_special[j]:
                            is_cant_id = True
                            break
                        if dest == 40 and 40 in horse_idxs:  # 40은 따로 처리해야함. special normal 둘다 포함
                            is_cant_id = True
                            break
                    if is_cant_id:
                        continue

                    horse_idxs[horse_id] = dest
                    if dest != -1:
                        back_track(n + 1, horse_idxs, horses_special, score + dest)
                    else:
                        back_track(n + 1, horse_idxs, horses_special, score)

            else:  # 평범 라인
                dest = find_destination(horse_idx, 0, move_num)
                for j in range(4):
                    if j == horse_id:
                        continue
                    if horse_idxs[j] == -1:
                        continue
                    if dest == horse_idxs[j] and not horses_special[j]:
                        is_cant_id = True
                        break
                    if dest == 40 and 40 in horse_idxs:  # 40은 따로 처리해야함. special normal 둘다 포함
                        is_cant_id = True
                        break
                if is_cant_id:
                    continue

                horse_idxs[horse_id] = dest
                if dest != -1:
                    back_track(n + 1, horse_idxs, horses_special, score + dest)
                else:
                    back_track(n + 1, horse_idxs, horses_special, score)


res_max = 0
back_track(0,[0,0,0,0],[0,0,0,0],0)
print(res_max)