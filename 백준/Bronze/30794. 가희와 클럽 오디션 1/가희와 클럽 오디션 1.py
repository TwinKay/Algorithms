import sys

data = sys.stdin.readline().split()
lv = int(data[0])
judgement = data[1]

if judgement == 'miss':
    print(0)
elif judgement == 'bad':
    print(200 * lv)
elif judgement == 'cool':
    print(400 * lv)
elif judgement == 'great':
    print(600 * lv)
elif judgement == 'perfect':
    print(1000 * lv)
