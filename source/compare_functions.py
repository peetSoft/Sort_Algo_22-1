def cmpr(x, y):
    """
    Compares x and y according to rules stated below.
    :param x: int
    :param y: int
    :return:
        -1 : x is even y is odd, or x and y are even or odd and x < y
         0 : x == y
         1 : x is odd y is even, or x and y are even or odd and x > y
    """
    if x % 2 < y % 2:
        return -1
    if x % 2 > y % 2:
        return 1
    if x < y:
        return -1
    if x > y:
        return 1
    if x == y:
        return 0
    return None

def my_cmpr(x, y): ##  docstring !
    if x < y:
        return -1
    if x > y:
        return 1
    if x == y:
        return 0

