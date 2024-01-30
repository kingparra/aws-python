from pint import UnitRegistry


ureg = UnitRegistry()
Q = ureg.Quantity


def area(h, w):
    result = Q(h) * Q(w)
    result = result.to("square meters")
    return result


def perim(h, w):
    result = 2 * (Q(h) + Q(w))
    result = result.to("meters")
    return result
