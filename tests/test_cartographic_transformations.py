from cartographic_transformations import jtsk_to_wgs84, wgs84_to_jtsk

EPS = 1e-3

def test_jtsk_to_wgs84():
    x, y = -868208.53, -1095793.57
    lon, lat = jtsk_to_wgs84(x, y)

    assert abs(lon - 12.8069888928) < EPS
    assert abs(lat - 49.4522627509) < EPS


def test_wgs84_to_jtsk():
    lon, lat = 79, -5
    x, y = wgs84_to_jtsk(lon, lat)

    assert (x - 8069383.78116) < EPS
    assert (y - (-5678083.75304)) < EPS
