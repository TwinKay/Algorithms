import sys

for line in sys.stdin:
    x_str, y_str = line.split()
    x, y = float(x_str), float(y_str)
    
    if x == 0 or y == 0:
        print("AXIS")
    elif x > 0 and y > 0:
        print("Q1")
    elif x < 0 and y > 0:
        print("Q2")
    elif x < 0 and y < 0:
        print("Q3")
    else:
        print("Q4")
    
    if x == 0 and y == 0:
        break
