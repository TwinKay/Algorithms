A, B, C, D = map(int, input().split())

shuttle = A + B <= D
walk = C <= D

if shuttle and walk:
    print("~.~")
elif not shuttle and not walk:
    print("T.T")
elif shuttle:
    print("Shuttle")
else:
    print("Walk")