A, B, C = map(int, input().split())

if A + B == C:
    print(f"{A}+{B}={C}")
elif A - B == C:
    print(f"{A}-{B}={C}")
elif A * B == C:
    print(f"{A}*{B}={C}")
elif B != 0 and A % B == 0 and A // B == C:
    print(f"{A}/{B}={C}")
elif B + C == A:
    print(f"{A}={B}+{C}")
elif B - C == A:
    print(f"{A}={B}-{C}")
elif B * C == A:
    print(f"{A}={B}*{C}")
elif C != 0 and B % C == 0 and B // C == A:
    print(f"{A}={B}/{C}")