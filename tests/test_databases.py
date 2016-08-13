from dbfpy import dbf
from grid import prepare_grid
from databases import get_measured_values, save_new_grid, add_records_to_shp, get_shapefile, save_new_shp, add_records_to_shp


EPS = 1e-3
pth = "tests/test_data/"

def test_get_measured_values():

    db = get_measured_values(pth + "concentration.dbf")
    db_fn = db.fieldNames   # fn ... field names

    assert 4 == len(db_fn)
    assert db_fn[0] == "BOD"
    assert db_fn[1] == "X"
    assert db_fn[2] == "Y"
    assert db_fn[3] == "N2_IHR"

    assert 4692 == db[0][0]
    # assert abs(4692 - db[0][0]) < EPS
    assert abs(-746650 - db[0][1]) < EPS
    assert abs(-1050750 - db[0][2]) < EPS
    assert abs(20.772 - db[0][3]) < EPS


def test_get_shapefile():

    sf, shapes, records, fields = get_shapefile(pth + "building_BMG_ID_76575.shp")

    assert 1 == len(shapes)
    assert 49 == len(shapes[0].points)
    assert 1 == len(records)
    assert 76575 == records[0][0] # id building
    assert 2 == records[0][1]     # num of resident
    assert 3 == len(fields)
    assert "BMG_ID" == fields[1][0]
    assert "OBYVATEL" == fields[2][0]


def test_save_new_grid():

    dic = {(0,0): 1.23}

    save_new_grid(pth + "new_concentration.dbf", dic)

    db = get_measured_values(pth + "new_concentration.dbf")
    db_fn = db.fieldNames   # fn ... field names

    assert 3 == len(db_fn)
    assert db_fn[0] == "X"
    assert db_fn[1] == "Y"
    assert db_fn[2] == "MEAS_VAL"

    # print db[0][0]
    assert 0 == db[0][0]
    assert 0 == db[0][1]
    assert abs(1.23 - db[0][2]) < EPS


def test_save_new_shp():

    sf, shapes, records, fields = get_shapefile(pth + "building_BMG_ID_76575.shp")
    records[0].append(25.687597)

    save_new_shp(pth + "new_building_BMG_ID_76575.shp", sf, shapes, records, fields)

    sf, shapes, records, fields = get_shapefile(pth + "new_building_BMG_ID_76575.shp")

    assert 1 == len(shapes)
    assert 49 == len(shapes[0].points)
    assert 1 == len(records)
    assert 76575 == records[0][0] # id building
    assert abs(25.687597 - records[0][2]) < EPS
    assert 2 == records[0][1]     # num of resident
    assert 4 == len(fields)
    assert "BMG_ID" == fields[1][0]
    assert "OBYVATEL" == fields[2][0]
    assert "KONCENTRAC" == fields[3][0]


def test_add_records_to_shp_centr_inside():

    db = get_measured_values(pth + "concentration.dbf")
    vec_x, vec_y, dic = prepare_grid(db)
    sf, shapes, records, fields = get_shapefile(pth + "building_BMG_ID_76575.shp")

    new_records = add_records_to_shp(vec_x, vec_y, dic, shapes, records)

    assert abs(25.687597 - new_records[0][2]) < EPS


def test_add_records_to_shp_centr_outside():

    db = get_measured_values(pth + "concentration.dbf")
    vec_x, vec_y, dic = prepare_grid(db)
    sf, shapes, records, fields = get_shapefile(pth + "building_BMG_ID_55065.shp")

    new_records = add_records_to_shp(vec_x, vec_y, dic, shapes, records)

    assert abs(-1 - new_records[0][2]) < EPS


