T = int(input())

for _ in range(T):
    lt, wt, le, we = map(int, input().split())

    area_telecom = lt * wt
    area_eurecom = le * we

    if area_telecom > area_eurecom:
        print("TelecomParisTech")
    elif area_telecom < area_eurecom:
        print("Eurecom")
    else:
        print("Tie")