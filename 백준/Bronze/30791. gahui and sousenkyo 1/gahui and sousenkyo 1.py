votes = list(map(int, input().split()))
vote_16th = votes[0]
competition_rate = sum(1 for vote in votes[1:] if vote_16th - vote <= 1000)

print(competition_rate)