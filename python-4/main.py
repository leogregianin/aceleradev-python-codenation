from math import degrees, atan2

def calc_angle_mbc(mb, bc):
    return int(round(degrees(atan2(mb, bc))))
