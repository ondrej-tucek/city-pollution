"""
This file contains functions that work with *.dbf and *.shp files.

"""

import shapefile
from dbfpy import dbf
from shapely.geometry import Polygon, Point

from interpolate import bilinear_intrp
from grid import find_square, add_corner_pt_to_dic


def get_measured_values(file_name):
    return dbf.Dbf(file_name, new=False)


def get_shapefile(file_name):
    sf = shapefile.Reader(file_name)
    shapes = sf.shapes()
    records = sf.records()
    fields = sf.fields

    return (sf, shapes, records, fields)


def save_new_grid(file_name, dic):
    col1 = "X"
    col2 = "Y"
    col3 = "MEAS_VAL"

    dbn = dbf.Dbf(file_name, new=True)
    dbn.addField((col1, "N", 15), (col2, "N", 15), (col3, "F", 19, 10))

    for el in dic.items():
        rec = dbn.newRecord()
        rec[col1] = el[0][0]
        rec[col2] = el[0][1]
        rec[col3] = el[1]
        rec.store()

    dbn.close()


def save_new_shp(file_name, sf, shapes, records, fields):
    col1 = "KONCENTRACE"

    w = shapefile.Writer()
    w.fields = list(fields)
    w.field(col1, "N", 13, 2)

    for rec in records:
        w.records.append(rec)

    w._shapes.extend(shapes)
    w.save(file_name)


def add_records_to_shp(vec_x, vec_y, dic, shapes, records):
    min_x = min(vec_x)
    max_x = max(vec_x)
    min_y = min(vec_y)
    max_y = max(vec_y)

    for (i, shp) in enumerate(shapes):
        pol = Polygon(shp.points).buffer(0)
        pt_centroid = pol.representative_point().coords[:]

        if min_x <= pt_centroid[0][0] <= max_x and min_y <=pt_centroid[0][1] <= max_y:
            (pt1, pt2, pt3, pt4) = find_square(pt_centroid[0], vec_x, vec_y)
            dic = add_corner_pt_to_dic(pt1, pt2, pt3, pt4, vec_x, vec_y, dic)
            val = bilinear_intrp(pt_centroid[0], pt1, pt2, pt3, pt4, dic)
            records[i].append(val)
        else:
            records[i].append(-1)

    return records


