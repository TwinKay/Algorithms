n_and_calls = input().split()
if len(n_and_calls) == 1:
    n = int(n_and_calls[0])
    call_times = list(map(int, input().split()))
else:
    n = int(n_and_calls[0])
    call_times = list(map(int, n_and_calls[1:]))

y_price = 0
m_price = 0

for time in call_times:
    y_price += 10 * (time // 30 + 1)
    m_price += 15 * (time // 60 + 1)

if y_price < m_price:
    print("Y", y_price)
elif y_price > m_price:
    print("M", m_price)
else:
    print("Y M", y_price)