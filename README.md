# Interpolation of pollution in Cities

This small project contains a couple of python's scripts which from measured values of pollution calculate values of pollution "inside buildings". This is a goal of this project. The main method is based on [bilinear interpolation](https://en.wikipedia.org/wiki/Bilinear_interpolation).


## Usage

Important notes: 
- if the [virtualenv](https://virtualenv.pypa.io/en/stable/), ([basic usage](http://docs.python-guide.org/en/latest/dev/virtualenvs/)) is installed skip step 1 below, otherwise install it
- some packages may depend on the order listed in requirements.txt or requirements_dev.txt

```
1. $ pip install virtualenv 
2. ~/virtuals$ virtualenv city-pollution
3. $ source ~/virtuals/city-pollution/bin/activate
4. $ source .envs
5. $ git clone git@github.com:ondrej-tucek/city-pollution.git
6. $ cd city-pollution
7. $ python app/app.py examples/data_in/buildings.shp examples/data_in/concentration.dbf examples/data_out/new_buildings.shp examples/data_out/new_concentration.dbf    
8. ... work now! ...
9. $ deactivate

```


## Results
Locations of measured pollution (red points).
<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/buildings_with_concentrations.png?raw=true" height="400" /></p>

Zoom of map, red points are locations of pollution, circles inside buildings are their centroids.
<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/buildings_with_their_centroids.png?raw=true" height="400" /></p>

Because original mesh is irregular, we had to do a rectangular. Now we can use bilinear interpolation method. On the img below is only view on a piece of mesh.
<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/mesh_for_bilinear_interpolation.png?raw=true" height="400" /></p>

Final result :simple_smile: 
<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/mesh_with_bilinear_interpolation_zoom.png?raw=true" height="400" /></p>


## Test
```
$ py.test -s -v --cov=app/ --durations=5 --cov-report term-missing
```

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/test_results.png?raw=true" height="200" /></p>
<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/building_76575_with_interpolated_concentration.png?raw=true" height="400" /></p>


## License
 [MIT](/LICENSE)

