# Population Grapher

## Prerequisites

* Download the following packages using pip

```
pip3 install numpy
```

```
pip3 install matplotlib
```

### Functionalities
* **Note:** This program was designed speicially for the NY state population csv (I have included it in the repository). For other data you can hard code in the cities or change the csv reader to read the specific rows you need. You will need a .csv file for whatever cities you are trying to plot.
* Use csv module to open csv file containing NY State city populations.
* Enter city names as input (**example:** Plattsburgh city, New York)
* Use matplotlib to plot the population data of the 3 cities entered. 
* A legend is displayed to show the cities and their corresponding line color and shape.

### Running population.py
* Make sure csv file is in same directory.
```
python3 population.py
```

* **Test Examples**
```
Enter the name of a city: Angola village, New York
```

```
Enter the name of another city: East Hampton village, New York
```

```
Enter a third city: Oswego city, New York
```

* Once the third city is entered, the graph will be displayed.

## Authors

* **Sean Reid** - [github](https://github.com/seankreid)
