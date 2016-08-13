# Interpolation of pollution in Cities

This small project contains a couple of python's scripts which from measured values of pollution calculate values of pollution "inside buildings". The main method is based on [bilinear interpolation](https://en.wikipedia.org/wiki/Bilinear_interpolation).

## Usage
````
1. $ pip install virtualenv 
2. ~/virtuals$ virtualenv `name_project`
3. $ source ~/virtuals/name_project/bin/activate
4. $ pip install cookiecutter
5. $ cd ~/projects/python/
6. $ cookiecutter git@github.com:ondrej-tucek/cookiecutter-python-project.git
7. fill the questions
8. put into requirements.txt or requirements_dev.txt file packages that you want/need it
9. $ pip install -r requirements_dev.txt
10. ... hard work now! ...
11. $ deactivate
$ source ~/virtuals/name_project/bin/activate
$ source .envs
$ python app/app.py examples/data_in/buildings.shp examples/data_in/concentration.dbf examples/data_out/new_buildings.shp examples/data_out/new_concentration.dbf
````


Important notes: 
- if the [virtualenv](https://virtualenv.pypa.io/en/stable/), ([basic usage](http://docs.python-guide.org/en/latest/dev/virtualenvs/)) is installed skip step 1 below
- some packages may depend on the order listed in requirements.txt or requirements_dev.txt


 




## Results
<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/buildings_with_concentrations.png?raw=true" height="400" /></p>

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/buildings_with_their_centroids.png?raw=true" height="400" /></p>

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/mesh_for_bilinear_interpolation.png?raw=true" height="400" /></p>

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/mesh_with_bilinear_interpolation_zoom.png?raw=true" height="400" /></p>



## Test
```
py.test -s -v --cov=app/ --durations=5 --cov-report term-missing
```

<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/test_results.png?raw=true" height="200" /></p>
<p align="center"><img src="https://github.com/ondrej-tucek/city-pollution/blob/master/docs/img/building_76575_with_interpolated_concentration.png?raw=true" height="400" /></p>



## License
 [MIT](/LICENSE)

