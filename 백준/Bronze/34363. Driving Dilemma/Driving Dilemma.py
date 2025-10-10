S = int(input())
D = float(input())
T = float(input())

speed = S * 5280 / 3600
distance = speed * T

if distance >= D:
    print("MADE IT")
else:
    print("FAILED TEST")
