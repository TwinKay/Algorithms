import sys, math

data = sys.stdin.buffer.read().split()
n = int(data[0])
cs = map(float, data[1:1+n])

V = math.fsum(c*c*c for c in cs)
x = V ** (1.0 / 3.0)
x = (2.0 * x + V / (x * x)) / 3.0

print(f"{x:.15f}")