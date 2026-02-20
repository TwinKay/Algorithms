import sys

for line in sys.stdin:
    M, A, B = map(int, line.split())
    if M == 0 and A == 0 and B == 0:
        break

    numerator = M * (B - A) * 3600
    denominator = A * B

    sec = (numerator + denominator // 2) // denominator

    H = sec // 3600
    sec %= 3600
    MM = sec // 60
    SS = sec % 60

    print(f"{H}:{MM:02d}:{SS:02d}")