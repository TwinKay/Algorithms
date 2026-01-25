h1, m1, s1 = map(int, input().split(':'))
h2, m2, s2 = map(int, input().split(':'))

t1 = h1 * 3600 + m1 * 60 + s1
t2 = h2 * 3600 + m2 * 60 + s2

if t2 > t1:
    wait = t2 - t1
elif t2 < t1:
    wait = 24 * 3600 - t1 + t2
else:
    wait = 24 * 3600

h = wait // 3600
wait %= 3600
m = wait // 60
s = wait % 60

print(f"{h:02d}:{m:02d}:{s:02d}")