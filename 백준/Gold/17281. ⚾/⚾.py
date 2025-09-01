'''
파이썬 재귀 진짜 너무하네;;;;;;
'''
import sys

N = int(sys.stdin.readline())
player_infos = []
for _ in range(N):
    player_infos.append(list(map(int, sys.stdin.readline().split())))

max_score = 0

visited = [0] * 9
for a in range(1, 9):
    visited[a] = 1
    for b in range(1, 9):
        if visited[b]: continue
        visited[b] = 1
        for c in range(1, 9):
            if visited[c]: continue
            visited[c] = 1
            for d in range(1, 9):
                if visited[d]: continue
                visited[d] = 1
                for e in range(1, 9):
                    if visited[e]: continue
                    visited[e] = 1
                    for f in range(1, 9):
                        if visited[f]: continue
                        visited[f] = 1
                        for g in range(1, 9):
                            if visited[g]: continue
                            visited[g] = 1
                            for h in range(1, 9):
                                if visited[h]: continue
                                visited[h] = 1

                                lst = [a, b, c, 0, d, e, f, g, h]
                                score = 0
                                player_num = 0
                                for ining in range(N):
                                    cnt_out = 0
                                    base_1 = 0
                                    base_2 = 0
                                    base_3 = 0
                                    while True:
                                        if player_infos[ining][lst[player_num % 9]] == 0:
                                            cnt_out += 1
                                            if cnt_out == 3:
                                                player_num += 1

                                                break
                                        elif player_infos[ining][lst[player_num % 9]] == 1:
                                            score += base_3
                                            base_3 = base_2
                                            base_2 = base_1
                                            base_1 = 1
                                        elif player_infos[ining][lst[player_num % 9]] == 2:
                                            score += base_3
                                            score += base_2
                                            base_3 = base_1
                                            base_2 = 1
                                            base_1 = 0
                                        elif player_infos[ining][lst[player_num % 9]] == 3:
                                            score += base_3
                                            score += base_2
                                            score += base_1
                                            base_3 = 1
                                            base_2 = 0
                                            base_1 = 0
                                        else:
                                            score += base_3
                                            score += base_2
                                            score += base_1
                                            score += 1
                                            base_3 = 0
                                            base_2 = 0
                                            base_1 = 0
                                        player_num += 1

                                max_score = max(max_score, score)

                                visited[h] = 0
                            visited[g] = 0
                        visited[f] = 0
                    visited[e] = 0
                visited[d] = 0
            visited[c] = 0
        visited[b] = 0
    visited[a] = 0

print(max_score)