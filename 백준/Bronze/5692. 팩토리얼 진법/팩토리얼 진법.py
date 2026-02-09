while True:
    s = input().strip()
    if s == '0':
        break

    result = 0
    fact = 1
    k = 1

    for i in range(len(s) - 1, -1, -1):
        result += int(s[i]) * fact
        k += 1
        fact *= k

    print(result)