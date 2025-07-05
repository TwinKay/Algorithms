w = int(input())
l = int(input())
h = int(input())

min_side = min(w, l)
max_side = max(w, l)

if min_side / h >= 2 and max_side / min_side <= 2:
    print("good")
else:
    print("bad")