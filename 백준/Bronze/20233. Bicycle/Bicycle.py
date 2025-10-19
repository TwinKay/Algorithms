a = int(input())
x = int(input())
b = int(input())
y = int(input())
T = int(input())

cost1 = a + max(0, T - 30) * x * 21
cost2 = b + max(0, T - 45) * y * 21
print(cost1, cost2)