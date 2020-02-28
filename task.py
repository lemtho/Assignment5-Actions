import math
from datetime import date


def firstrun():
    return "success"


def circle(radius):
    area = radius ** 2 * math.pi
    return round(area, 2)


def firstlast(e_list):
    return [e_list[0], e_list[-1]]


def daysbetween(year1, month1, day1, year2, month2, day2):
    first_date = date(year1, month1, day1)
    second_date = date(year2, month2, day2)
    delta = second_date - first_date
    return delta.days
