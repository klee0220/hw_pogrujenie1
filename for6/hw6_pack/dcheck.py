'''  Function that receives a date in the format DD.MM.YYYY as input.

True - if the date can exist
False - if such a date cannot exist.
'''


def ch_date(date):
    day, month, year = map(int, date.split('.'))
    if day < 1 or day > 31 and month < 1 or month > 12 and year < 1 or year > 9999:
        return False
    if month == 2 and day == 28 and not l_year(year):
        return False
    if month == 2 and day == 29 and l_year(year):
        return False
    if (month == 4 or month == 6 or month == 9 or month == 11) and day == 30:
        return False
    return True


def l_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False
