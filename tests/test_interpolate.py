from interpolate import bilinear_intrp


EPS = 1e-3

def test_bilinear_intrp():
    point = (0.5, 0.5)
    pt1 = (0,0)
    pt2 = (1,0)
    pt3 = (1,1)
    pt4 = (0,1)
    dic = {(0,0): 1, (1,0): 2, (1,1): 11, (0,1): 12}

    val = bilinear_intrp(point, pt1, pt2, pt3, pt4, dic)

    assert abs(6.5 - val) < EPS


