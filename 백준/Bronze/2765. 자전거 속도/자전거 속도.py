import sys

INCH_PER_MILE = 5280 * 12

trip = 1
for line in sys.stdin:
    d, r, t = map(float, line.split())
    r = int(r)

    if r == 0:
        break

    distance = 3.1415927 * d * r / INCH_PER_MILE

    time_hour = t / 3600
    mph = distance / time_hour

    print(f"Trip #{trip}: {distance:.2f} {mph:.2f}")
    trip += 1