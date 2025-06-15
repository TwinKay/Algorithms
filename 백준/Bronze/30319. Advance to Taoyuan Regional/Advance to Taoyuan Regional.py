year, month, day = map(int, input().split('-'))
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

acc_days = [0] * 13
for i in range(1, 13):
    acc_days[i] = acc_days[i - 1] + month_days[i]

base_day = acc_days[9] + 16
input_day = acc_days[month] + day

if input_day > base_day:
    print("TOO LATE")
else:
    print("GOOD")