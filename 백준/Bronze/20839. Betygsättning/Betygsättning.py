x, y, z = map(int, input().split())
xa, yc, ze = map(int, input().split())

if xa == x and yc == y and ze == z:
    print("A")
elif yc == y and ze == z and xa * 2 >= x:
    print("B")
elif yc == y and ze == z:
    print("C")
elif ze == z and yc * 2 >= y:
    print("D")
else:
    print("E")