t1, m1, t2, m2 = map(int, input().split())

start = t1 * 60 + m1
end = t2 * 60 + m2

if end >= start:
    diff = end - start
else:
    diff = 1440 - start + end

n = diff // 30

print(diff, n)
