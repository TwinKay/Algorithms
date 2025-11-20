a = input().strip()
b = input().strip()

ah, am = map(int, a.split(':'))
bh, bm = map(int, b.split(':'))

a_time = ah * 60 + am
b_time = bh * 60 + bm

print("YES" if b_time > a_time else "NO")