h, m = map(int, input().split())
t = int(input())
total = h*60 + m
total = total+t
if total >= 24*60:
    total = total - 24*60
print(str(total//60)+" "+str(total%60))