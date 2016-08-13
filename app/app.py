#!/usr/bin/env python
# -*- coding: utf-8 -*-

import click
import sys
sys.path.append('city_pollution')

# import numpy as np
from shapely.geometry import Polygon, Point

from grid import prepare_grid
from databases import get_measured_values, get_shapefile, save_new_shp, save_new_grid, add_records_to_shp


@click.command()
@click.argument('fn_shp', nargs=1)
@click.argument('fn_meas_val', nargs=1)
@click.argument('fn_new_shp', nargs=1)
@click.argument('fn_new_meas_val', nargs=1)


def main(fn_shp, fn_meas_val, fn_new_shp, fn_new_meas_val):
    """
    Args:
        fn_shp: have to contain a path to shapefile and shapefile's name
        fn_meas_val: again, have to contain a path and database file of measured values, f.e. pollution.dbf
        new_...: similar as previous

    Use:
        python app/app.py examples/data_in/buildings.shp examples/data_in/concentration.dbf examples/data_out/new_buildings.shp examples/data_out/new_concentration.dbf

    """

    print
    db_kon = get_measured_values(fn_meas_val)
    sf, shapes, records, fields = get_shapefile(fn_shp)
    vec_x, vec_y, dic = prepare_grid(db_kon)

    new_records = add_records_to_shp(vec_x, vec_y, dic, shapes, records)

    save_new_shp(fn_new_shp, sf, shapes, new_records, fields)
    print "Save: new_shp... done."

    save_new_grid(fn_new_meas_val, dic)
    print "Save: new_grid... done."
    print
    print "This is the END..."
    print


if __name__ == '__main__':
    main()
