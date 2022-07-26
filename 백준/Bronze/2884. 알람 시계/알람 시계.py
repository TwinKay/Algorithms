h, m = map(int, input().split())
total = h*60 + m
if total < 45:
    print("23 "+str(total+15))
else:
    total = total-45
    print(str(total//60)+" "+str(total%60))