def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def get_days_in_month(year,month):
    if is_leap_year(year):
        if month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        else:
            return 29
    else:
        if month == 4 or month == 6 or month == 9 or month == 11:
            return 30
        elif month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            return 31
        else:
            return 28

def get_start_day(year,month):
    if month == 1:
        month += 12
        year -= 1
    elif month == 2:
        month += 12
        year -= 1
    k = year % 100
    j = year // 100
    # print(k,'--',j)
    day = (1 + (13 * (month + 1)) // 5 + k + k // 4 + j // 4 + 5 * j ) % 7
    return (day + 5 ) % 7

def display_calendar(year,month):
    day = get_days_in_month(year,month)
    number = get_start_day(year,month)
    print(day,'--',number)
    print(f'   {year}年{month}月')
    print('Mo Tu We Th Fr Sa Su')
    print('   '* number ,end = '')
    for day in range(1,day + 1):
        print(f'{day:2}',end = ' ')
        if (number + day ) % 7 == 0:
            print()
    print()
    
# print(is_leap_year(2020))
# print(is_leap_year(1900))
# print(is_leap_year(2000))

# print('--'*30)

# print(get_days_in_month(2020,2))
# print(get_days_in_month(2021,2))
# print(get_days_in_month(2021,4))
# print(get_days_in_month(2021,12))

# print('--'*30)

# print(get_start_day(2023,11))
# print(get_start_day(2024,2))
# print('--'*30)


display_calendar(2023,11)
print('--'*15)
display_calendar(2024,3)
