s = int(input())
a = int(input())
b = int(input())

k = 0 if s <= a else (s - a + b - 1) // b
print(250 + 100 * k)