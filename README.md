# Interpolation of pollution in Cities

description here


## Usage
````
source .envs
python app/app.py examples/data_in/buildings.shp examples/data_in/concentration.dbf examples/data_out/new_buildings.shp examples/data_out/new_concentration.dbf
````

## Results
<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/buildings_with_concentrations.png?raw=true" height="400" /></p>

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/buildings_with_their_centroids.png?raw=true" height="400" /></p>

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/mesh_for_bilinear_interpolation.png?raw=true" height="400" /></p>

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/mesh_with_bilinear_interpolation_zoom.png?raw=true" height="400" /></p>










##Testing
```
py.test -s -v --cov=app/ --durations=5 --cov-report term-missing
```

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/building_76575_with_interpolated_concentration.png?raw=true" height="400" /></p>

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/test_results.png?raw=true" height="400" /></p>


## License
 [MIT](/LICENSE)

