N = int(input())

for _ in range(N):
    sid, s1, s2, s3 = input().split()
    s1, s2, s3 = map(int, [s1, s2, s3])
    
    total = s1 + s2 + s3
    ok1 = s1 >= 11
    ok2 = s2 >= 8
    ok3 = s3 >= 12
    ok_total = total >= 55
    
    if ok1 and ok2 and ok3 and ok_total:
        result = "PASS"
    else:
        result = "FAIL"
    
    print(sid, total, result)