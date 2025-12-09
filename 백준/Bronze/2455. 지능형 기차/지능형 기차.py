import sys

current = 0
max_people = 0

for _ in range(4):
    out_count, in_count = map(int, sys.stdin.readline().split())
    current -= out_count
    current += in_count
    if current > max_people:
        max_people = current

print(max_people)