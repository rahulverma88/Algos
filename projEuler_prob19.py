
days_month = [31, 28, 31,30, 31, 30, 31, 31, 30, 31, 30, 31]

year = 1901
day = 0
num_sundays = 0

while year < 2001:
    for i in range(len(days_month)):
        day += days_month[i]
        if year % 4 == 0 and year % 100 != 0 and i == 1:
            day += 1
        elif year % 400 == 0 and i == 1:
            day += 1

        if (day + 2) % 7 == 0:
            num_sundays += 1

    year += 1

print(num_sundays)
