import math

w, h = map(int, input().split())
n, a, b = map(int, input().split())

if a > w or b > h:
    print(-1)
else:
    letters_per_row = w // a
    rows_per_page = h // b
    letters_per_page = letters_per_row * rows_per_page

    if letters_per_page == 0:
        print(-1)
    else:
        pages_needed = math.ceil(n / letters_per_page)
        print(pages_needed)
