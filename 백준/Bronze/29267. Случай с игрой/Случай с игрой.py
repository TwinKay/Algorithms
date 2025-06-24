n, k = map(int, input().split())
actions = [input().strip() for _ in range(n)]

ammo = 0
saved = 0
has_save = False

for action in actions:
    if action == "ammo":
        ammo += k
    elif action == "save":
        saved = ammo
        has_save = True
    elif action == "load":
        ammo = saved if has_save else 0
    elif action == "shoot":
        if ammo > 0:
            ammo -= 1
    print(ammo)