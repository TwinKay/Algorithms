start = input().strip()
end = input().strip()

sh, sm, ss = map(int, start.split(" : "))
eh, em, es = map(int, end.split(" : "))

start_seconds = sh * 3600 + sm * 60 + ss
end_seconds = eh * 3600 + em * 60 + es

if end_seconds < start_seconds:
    end_seconds += 24 * 3600

print(end_seconds - start_seconds)