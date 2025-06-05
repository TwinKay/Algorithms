n, m, k, a, b, c = map(int, input().split())

joffrey_soldiers = n * a
robb_soldiers = m * b
stannis_soldiers = k * c

max_soldiers = max(joffrey_soldiers, robb_soldiers, stannis_soldiers)

result = []
if joffrey_soldiers == max_soldiers:
    result.append("Joffrey")
if robb_soldiers == max_soldiers:
    result.append("Robb")
if stannis_soldiers == max_soldiers:
    result.append("Stannis")

print(" ".join(sorted(result)))