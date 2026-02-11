while True:
    N = int(input())
    if N == 0:
        break
    
    result = N * (N + 1) * (2 * N + 1) // 6
    print(result)