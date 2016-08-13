"""
This file contains functions for work with a grid.
"""

def prepare_grid(db):
    """
    Return two vectors of coordinates x, y
    and measured values in these coordinates.
    """

    vec_x = set()
    vec_y = set()
    dic = {}

    for el in db:
        dic[(el[1], el[2])] = el[3]
        vec_x.add(el[1])
        vec_y.add(el[2])

    return (sorted(vec_x), sorted(vec_y), dic)


def find_square(centroid, axis_x, axis_y):
    """
    Return four points (corners of a square) in which
    is located point so-called a centroid.
    """

    axis_x = zip(axis_x, tuple(axis_x)[1:])
    axis_y = zip(axis_y, tuple(axis_y)[1:])

    # optimalizace s reduce
    x1, x2 = filter(lambda p: p[0] <= centroid[0] <= p[1], axis_x)[0]
    y1, y2 = filter(lambda p: p[0] <= centroid[1] <= p[1], axis_y)[0]

    return ((x1,y1), (x2,y1), (x2,y2), (x1,y2))


def add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic):
    """
    Return dictionary of measured values and
    also new averaged measured values.
    """

    min_x = min(vec_x)
    max_x = max(vec_x)
    min_y = min(vec_y)
    max_y = max(vec_y)

    for (i, pt) in enumerate([pt1, pt2, pt3, pt4]):
        try:
            dic[pt]
        except KeyError:
            # print pt1, pt2, pt3, pt4
            if i == 0:
                if pt1[0] == min_x and pt1[1] == min_y:
                    dic[pt1] = (dic[pt4] + dic[pt2])/2
                elif pt1[0] == min_x:
                    idy = vec_y.index(pt1[1])
                    dic[pt1] = (dic[pt2] + dic[(pt1[0], vec_y[idy-1])])/2
                else:
                    idx = vec_x.index(pt1[0])
                    dic[pt1] = (dic[pt2] + dic[(vec_x[idx-1], pt1[1])])/2

            elif i == 1:
                if pt2[0] == max_x and pt2[1] == min_y:
                    dic[pt2] = (dic[pt1] + dic[pt3])/2
                elif pt2[0] == max_x:
                    idy = vec_y.index(pt2[1])
                    dic[pt2] = (dic[pt1] + dic[(pt2[0], vec_y[idy-1])])/2
                else:
                    idx = vec_x.index(pt2[0])
                    dic[pt2] = (dic[pt1] + dic[(vec_x[idx+1], pt2[1])])/2

            elif i == 2:
                if pt3[0] == max_x and pt3[1] == max_y:
                    dic[pt3] = (dic[pt4] + dic[pt2])/2
                elif pt3[0] == max_x:
                    dic[pt3] = (dic[pt4] + dic[pt2])/2
                    # idy = vec_y.index(pt3[1]
                    # dic[pt3] = (dic[pt4] + dic[(pt3[0], vec_y(idy+1))])/2
                else:
                    idx = vec_x.index(pt3[0])
                    dic[pt3] = (dic[pt4] + dic[(vec_x[idx+1], pt3[1])])/2

            elif i == 3:
                if pt4[0] == min_x and pt4[1] == max_y:
                    dic[pt4] = (dic[pt1] + dic[pt3])/2
                elif pt4[0] == min_x:
                    dic[pt4] = (dic[pt1] + dic[pt3])/2
                    # idy = vec_y.index(pt4[1])
                    # dic[pt4] = (dic[pt3] + dic[(pt4[0], vec_y[idy+1])])/2
                else:
                    idx = vec_x.index(pt4[0])
                    dic[pt4] = (dic[pt3] + dic[(vec_x[idx-1], pt4[1])])/2
    return dic

