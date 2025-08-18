import sys

def get_dist(idx1,idx2):
    x1,y1 = idx1
    x2,y2 = idx2
    return abs(x2-x1) + abs(y2-y1)

left_keyboard = dict()
right_keyboard = dict()
left_keyboard['q'] = (0,0)
left_keyboard['w'] = (0,1)
left_keyboard['e'] = (0,2)
left_keyboard['r'] = (0,3)
left_keyboard['t'] = (0,4)

left_keyboard['a'] = (1,0)
left_keyboard['s'] = (1,1)
left_keyboard['d'] = (1,2)
left_keyboard['f'] = (1,3)
left_keyboard['g'] = (1,4)

left_keyboard['z'] = (2,0)
left_keyboard['x'] = (2,1)
left_keyboard['c'] = (2,2)
left_keyboard['v'] = (2,3)

right_keyboard['y'] = (0,1)
right_keyboard['u'] = (0,2)
right_keyboard['i'] = (0,3)
right_keyboard['o'] = (0,4)
right_keyboard['p'] = (0,5)

right_keyboard['h'] = (1,1)
right_keyboard['j'] = (1,2)
right_keyboard['k'] = (1,3)
right_keyboard['l'] = (1,4)

right_keyboard['b'] = (2,0)
right_keyboard['n'] = (2,1)
right_keyboard['m'] = (2,2)

left,right = sys.stdin.readline().split()
left_idx, right_idx = left_keyboard[left], right_keyboard[right]
queries = list(sys.stdin.readline().rstrip())
res = 0
for query in queries:
    if query in left_keyboard.keys():
        next_left_idx = left_keyboard[query]
        dist = get_dist(left_idx,next_left_idx)
        res += dist
        left_idx = next_left_idx
    else:
        next_right_idx = right_keyboard[query]
        dist = get_dist(right_idx, next_right_idx)
        res += dist
        right_idx = next_right_idx

print(res + len(queries))