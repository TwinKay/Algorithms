Ca, Ba, Pa = map(int, input().split())
Cr, Br, Pr = map(int, input().split())

ans = 0
ans += max(Cr - Ca, 0)
ans += max(Br - Ba, 0)
ans += max(Pr - Pa, 0)

print(ans)