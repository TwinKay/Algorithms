import sys

T = int(sys.stdin.readline().strip())
scores = list(map(int, input().split()))
while len(scores) < 5:
    scores.append(0)
korean, math, english, inquiry, second = scores

if korean > english:
    v1 = (korean - english) * 508
else:
    v1 = (english - korean) * 108

if math > inquiry:
    v2 = (math - inquiry) * 212
else:
    v2 = (inquiry - math) * 305

v3 = second * 707

student_id = (v1 + v2 + v3) * 4763
print(student_id)