import math

case = 1

while True:
    a, b, c = map(int, input().split())
    
    if a == 0 and b == 0 and c == 0:
        break
    
    print(f"Triangle #{case}")
    
    if a == -1:
        if c <= b:
            print("Impossible.")
        else:
            value = math.sqrt(c*c - b*b)
            print(f"a = {value:.3f}")
    
    elif b == -1:
        if c <= a:
            print("Impossible.")
        else:
            value = math.sqrt(c*c - a*a)
            print(f"b = {value:.3f}")
    
    elif c == -1:
        value = math.sqrt(a*a + b*b)
        print(f"c = {value:.3f}")
    
    print()
    case += 1