while True:
    try:
        line = input().strip()
        if line == "0":
            break
        num = float(line)
        
        wives = num
        sacks = wives * num
        cats = sacks * num
        kittens = cats * num
        total = 1 + wives + sacks + cats + kittens

        print(f"{total:.2f}")

    except EOFError:
        break
