env, poster, info = map(int, input().split())

C4 = 0.229 * 0.324
A3 = 0.297 * 0.420
A4 = 0.210 * 0.297

weight = env * C4 * 2 + poster * A3 * 2 + info * A4

print(f"{weight:.6f}")