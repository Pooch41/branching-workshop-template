M_IN_KM = 1000


def square_meters_to_square_kilometers(meters):
    """takes meters (int/float) and returns kilometers (float)"""
    return meters / (M_IN_KM ** 2)
