"""
This file contains bilinear interpolation function.
"""

def bilinear_intrp(point, pt1, pt2, pt3, pt4, dic):
    """
    Return computed value from unknown function f
    at point (x, y).

    Args:
        point: is pt_centroid, where we want to find
            a value of f(x,y).
        pt1 = Q11, pt2 = Q21, pt3 = Q22, pt4 = Q12
        fQij: Contains known the values of f at the four
            points Qij with coords x, y.
        Qij = (xi, yj), f.e. Q12 = (x1, y2),...
    """

    x = point[0]
    y = point[1]

    x1 = pt1[0]
    y1 = pt1[1]
    x2 = pt3[0]
    y2 = pt3[1]
    fQ11 = dic[pt1]
    fQ21 = dic[pt2]
    fQ22 = dic[pt3]
    fQ12 = dic[pt4]

    return (fQ11*(x2-x)*(y2-y) + fQ21*(x-x1)*(y2-y) + \
            fQ12*(x2-x)*(y-y1) + fQ22*(x-x1)*(y-y1))/((x2-x1)*(y2-y1))

