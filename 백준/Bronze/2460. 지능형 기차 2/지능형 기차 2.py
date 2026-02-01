current = 0
max_people = 0

for _ in range(10):
    out_, in_ = map(int, input().split())
    current -= out_
    current += in_
    max_people = max(max_people, current)

print(max_people)