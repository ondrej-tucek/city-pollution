"""
This file contains cartographic transformations.
For more details see page
http://freegis.fsv.cvut.cz/gwiki/S-JTSK
"""

from pyproj import Proj, transform


def jtsk_to_wgs84(x, y):
    """
    Return tuple (lon, lat) coordinates.

    Use:
        x, y = -868208.53, -1095793.57
        lon, lat = jtsk_to_wgs84(x, y)
        print lon, lat

    """

    jtsk = Proj("+proj=krovak +ellps=bessel +towgs84=570.8,85.7,462.8,4.998,1.587,5.261,3.56")
    wgs84 = Proj("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")

    # alternatively you can use
    # wgs84 = Proj(init='epsg:4326')
    # jtsk = Proj(init='epsg:5514') # S-JTSK East North (Greenwitch)
    # jtsk = Proj(init='epsg:2065') # S-JTSK South West (Ferro)

    return transform(jtsk, wgs84, x, y)


def wgs84_to_jtsk(lon, lat):
    """
    Return tuple (x, y) coordinates.

    Use:
        lon, lat = 79, -5
        x, y = wgs84_to_jtsk(lon, lat)
        print x, y

    """

    jtsk = Proj("+proj=krovak +ellps=bessel +towgs84=570.8,85.7,462.8,4.998,1.587,5.261,3.56")
    wgs84 = Proj("+proj=longlat +ellps=WGS84 +datum=WGS84 +no_defs")

    return transform(wgs84, jtsk, lon, lat)

