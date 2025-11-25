p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

aggregate_persepolis = p1 + p2 
aggregate_esteghlal = s1 + s2  

away_goals_persepolis = p2 
away_goals_esteghlal = s1

if aggregate_persepolis > aggregate_esteghlal:
    print("Persepolis")
elif aggregate_persepolis < aggregate_esteghlal:
    print("Esteghlal")
else:
    if away_goals_persepolis > away_goals_esteghlal:
        print("Persepolis")
    elif away_goals_persepolis < away_goals_esteghlal:
        print("Esteghlal")
    else:
        print("Penalty")