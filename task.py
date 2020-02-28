import math


def firstrun():
    return "success"


def circle(radius):
    area = radius ** 2 * math.pi
    return round(area, 2)


def firstlast(e_list):
    return [e_list[0], e_list[-1]]