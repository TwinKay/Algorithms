good_score = [1, 2, 3, 3, 4, 10]
evil_score = [1, 2, 2, 2, 3, 5, 10]

T = int(input())

for t in range(1, T + 1):
    good = list(map(int, input().split()))
    evil = list(map(int, input().split()))

    good_sum = sum(g * s for g, s in zip(good, good_score))
    evil_sum = sum(e * s for e, s in zip(evil, evil_score))

    if good_sum > evil_sum:
        result = "Good triumphs over Evil"
    elif good_sum < evil_sum:
        result = "Evil eradicates all trace of Good"
    else:
        result = "No victor on this battle field"

    print(f"Battle {t}: {result}")