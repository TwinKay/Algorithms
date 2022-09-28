import sys

n = int(sys.stdin.readline())

paper = []
for _ in range(n):
    paper.append(list(map(int, sys.stdin.readline().split())))

w=0
b=0

def cut(x,y,n):
    global w,b
    dst = set()
    for i in range(x,x+n):
        for j in range(y,y+n):
            dst.add(paper[i][j])

    if len(dst) != 1:
        cut(x, y, n//2)
        cut(x, y + n//2, n//2)
        cut(x + n//2, y, n//2)
        cut(x + n//2, y + n//2, n//2)
        return

    else:
        dst = list(dst)
        if dst[0] == 0:
            w += 1
        else:
            b += 1

cut(0,0,n)
print(w)
print(b)