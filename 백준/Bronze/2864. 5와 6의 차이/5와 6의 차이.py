import sys

a,b = sys.stdin.readline().split()

a_1 = a.replace('5','6')
b_1 = b.replace('5','6')
a_2 = a.replace('6','5')
b_2 = b.replace('6','5')

print(int(a_2)+int(b_2), end = ' ')
print(int(a_1)+int(b_1))