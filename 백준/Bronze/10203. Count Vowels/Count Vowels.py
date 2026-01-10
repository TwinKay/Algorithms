t = int(input())
vowels = {'a', 'e', 'i', 'o', 'u'}

for _ in range(t):
    word = input().strip()
    count = 0
    for c in word:
        if c in vowels:
            count += 1
    print(f"The number of vowels in {word} is {count}.")