cubes = [i ** 3 for i in range(101)]

for a in range(2, 101):
    a3 = cubes[a]
    for b in range(2, a):
        b3 = cubes[b]
        for c in range(b + 1, a):
            bc3 = b3 + cubes[c]
            if bc3 >= a3:
                break
            for d in range(c + 1, a):
                if bc3 + cubes[d] == a3:
                    print(f"Cube = {a}, Triple = ({b},{c},{d})")