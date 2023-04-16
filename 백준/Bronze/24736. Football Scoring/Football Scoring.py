import sys

a,b,c,d,e = map(int, sys.stdin.readline().split())
f,g,h,i,j = map(int, sys.stdin.readline().split())

x = a*6+b*3+c*2+d+e*2
y = f*6+g*3+h*2+i+j*2
print(str(x)+' '+str(y))