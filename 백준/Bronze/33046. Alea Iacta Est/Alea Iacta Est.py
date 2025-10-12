A, B = map(int, input().split())
C, D = map(int, input().split())

S1 = A + B
fake = (1 + (S1 - 1)) % 4
if fake == 0:
    fake = 4

S2 = C + D
true = (fake + (S2 - 1)) % 4
if true == 0:
    true = 4

print(true)
