day = int(input())
count_year = 0
count_week = 0
if day >= 365:
    count_year = day // 365
    day -= 365 * count_year
if day >= 7:
    count_week = day // 7
    day -= 7 * count_week

print(count_year, count_week, day, sep=" ", end="")