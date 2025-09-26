import sys

def get_result(lst):
    for l in lst:
        if l < 48:
            return 'False'
    return 'True'


N = int(sys.stdin.readline())
lst = []
for _ in range(N):
    lst.append(int(sys.stdin.readline()))
print(get_result(lst))