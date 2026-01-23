t = int(input())

for tc in range(t):
    n = int(input())
    
    print('#' * n)
    
    for _ in range(n - 2):
        print('#' + 'J' * (n - 2) + '#')

    if n > 1:
        print('#' * n)

    if tc != t - 1:
        print()