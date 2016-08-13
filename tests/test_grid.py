
from grid import prepare_grid, find_square, add_corner_pt_to_dic
from databases import get_measured_values


EPS = 1e-3
pth = "tests/test_data/"

def test_prepare_grid():

    db = get_measured_values(pth + "concentration.dbf")

    vec_x, vec_y, dic = prepare_grid(db)

    assert isinstance(vec_x,(list,tuple))
    assert isinstance(vec_y,(list,tuple))
    assert isinstance(dic,dict)

    assert (-746800) in vec_x
    assert (-1050750) in vec_y
    assert (-740350, -1047750) in dic


def test_find_square():

    db = get_measured_values(pth + "concentration.dbf")
    vec_x, vec_y, dic = prepare_grid(db)

    pt_centroid = (-745052, -1050189)
    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    assert pt1 == (-745150, -1050250)
    assert pt2 == (-745000, -1050250)
    assert pt3 == (-745000, -1050000)
    assert pt4 == (-745150, -1050000)


# =============== Test if pt1 is in dic ================

def test_add_corner_pt_to_dic_pt1_if():

    pt_centroid = (-746746, -1050660)

    db = get_measured_values(pth + "concentration.dbf")
    vec_x, vec_y, dic = prepare_grid(db)
    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt1 in dic
    assert abs((19.581 + 20.772)/2 - dic[pt1]) < EPS


def test_add_corner_pt_to_dic_pt1_elif():

    pt_centroid = (-746746, -1050130)

    db = get_measured_values(pth + "concentration.dbf")
    vec_x, vec_y, dic = prepare_grid(db)
    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt1 in dic
    assert abs((19.035+ 19.581)/2 - dic[pt1]) < EPS


def test_add_corner_pt_to_dic_pt1_else():

    pt_centroid = (-746570, -1050375)

    db = get_measured_values(pth + "concentration.dbf")
    vec_x, vec_y, dic = prepare_grid(db)
    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt1 in dic
    assert abs((19.581 + 19.760)/2 - dic[pt1]) < EPS


# =============== Test if pt2 is in dic ================

def test_add_corner_pt_to_dic_pt2_if():

    dic = {}
    pt_centroid = (0.5, 0.5)
    vec_x = [0, 1]
    vec_y = [0, 1]
    dic[(0,0)] = 1.0    # pt1
    dic[(1,1)] = 3.0    # pt3

    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt2 in dic
    assert abs((1.0 + 3.0)/2 - dic[pt2]) < EPS


def test_add_corner_pt_to_dic_pt2_elif():

    dic = {}
    pt_centroid = (0.5, 1.5)
    vec_x = [0, 1]
    vec_y = [0, 1, 2]
    dic[(0,1)] = 1.0    # pt1
    dic[(1,0)] = 2.0
    dic[(1,2)] = 3.0    # pt3

    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt2 in dic
    assert abs((1.0 + 2.0)/2 - dic[pt2]) < EPS


def test_add_corner_pt_to_dic_pt2_else():

    dic = {}
    pt_centroid = (0.5, 0.5)
    vec_x = [0, 1, 2]
    vec_y = [0, 1]
    dic[(0,0)] = 1.0    # pt1
    dic[(2,0)] = 2.0
    dic[(1,1)] = 3.0    # pt3

    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt2 in dic
    assert abs((1.0 + 2.0)/2 - dic[pt2]) < EPS



# =============== Test if pt3 is in dic ================

def test_add_corner_pt_to_dic_pt3_if():

    dic = {}
    pt_centroid = (0.5, 0.5)
    vec_x = [0, 1]
    vec_y = [0, 1]
    dic[(1,0)] = 1.0    # pt2
    dic[(0,1)] = 3.0    # pt4

    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt3 in dic
    assert abs((1.0 + 3.0)/2 - dic[pt3]) < EPS


def test_add_corner_pt_to_dic_pt3_elif():

    dic = {}
    pt_centroid = (0.5, 0.5)
    vec_x = [0, 1]
    vec_y = [0, 1, 2]
    dic[(1,0)] = 1.0    # pt2
    dic[(0,1)] = 3.0    # pt4
    dic[(1,2)] = 2.0

    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt3 in dic
    assert abs((1.0 + 3.0)/2 - dic[pt3]) < EPS


def test_add_corner_pt_to_dic_pt3_else():

    dic = {}
    pt_centroid = (0.5, 0.5)
    vec_x = [0, 1, 2]
    vec_y = [0, 1]
    dic[(1,0)] = 1.0    # pt2
    dic[(0,1)] = 2.0    # pt4
    dic[(2,1)] = 3.0

    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt3 in dic
    assert abs((2.0 + 3.0)/2 - dic[pt3]) < EPS


# =============== Test if pt4 is in dic ================

def test_add_corner_pt_to_dic_pt4_if():

    dic = {}
    pt_centroid = (0.5, 0.5)
    vec_x = [0, 1]
    vec_y = [0, 1]
    dic[(0,0)] = 1.0    # pt1
    dic[(1,1)] = 3.0    # pt3

    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt4 in dic
    assert abs((1.0 + 3.0)/2 - dic[pt4]) < EPS


def test_add_corner_pt_to_dic_pt4_elif():

    dic = {}
    pt_centroid = (0.5, 0.5)
    vec_x = [0, 1]
    vec_y = [0, 1, 2]
    dic[(0,0)] = 1.0    # pt1
    dic[(1,1)] = 3.0    # pt3

    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt4 in dic
    assert abs((1.0 + 3.0)/2 - dic[pt4]) < EPS


def test_add_corner_pt_to_dic_pt4_else():

    dic = {}
    pt_centroid = (1.5, 0.5)
    vec_x = [0, 1, 2]
    vec_y = [0, 1]
    dic[(0,1)] = 2.0
    dic[(1,0)] = 1.0    # pt1
    dic[(2,1)] = 3.0    # pt3

    (pt1, pt2, pt3, pt4) = find_square(pt_centroid, vec_x, vec_y)

    dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)

    assert pt4 in dic
    assert abs((2.0 + 3.0)/2 - dic[pt4]) < EPS


