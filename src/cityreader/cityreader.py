import csv

# Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


class City:
    def __init__(self, name, lat, lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def __str__(self):
        return f"{self.name}, {self.lat}-{self.lat} "


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
cities = []


def cityreader(cities=[]):
    with open('/Users/Pariah/lambda/Sprint-Challenge--Intro-Python/src/cityreader/cities.csv', 'r') as csvfile:
        dump = csv.reader(csvfile)  # create a readable dump
        next(dump)  # do not add first line
    # Implement the functionality to read from the 'cities.csv' file
    # For each city record, create a new City instance and add it to the
    # `cities` list
        for row in dump:  # line = rows
            cities.append(City(row[0], float(row[3]), float(row[4])))

    return cities


cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square.

# Pass these latitude and longitude values as parameters to the `cityreader_stretch` function, along with the `cities` list that holds all the City instances from the `cityreader` function. This function should output all the cities that fall within the coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)


# first_lat = input("enter the first latitude")
# first_lon = input("enter the first longitude")
# second_lat = input("enter the second latitude")
# second_lon = input("enter the second longitude")


# figure out how to form the WMO Square: Square formation pos/neg, pos/pos, neg/pos, neg/neg in that order

#  get the input:
first_loc = input(
    "please enter your first set of coordinates, please include a comma in between them: ")
second_loc = input(
    "please enter your second set of coordinates, please include a comma in betwen them: ")

# Ensure that the lat and lon values are floats (user input change into floats)
# float both input numbers


def floatomatic(a, b):
    # set the numbers to a variable
    itemize = f"{a},{b}"
    # return the float version of those numbers, split at the comma
    # must be a list --  i think I keep getting a subscriptable error
    return [float(num) for num in itemize.split(",")]


# set the values to a variable:
box = floatomatic(first_loc, second_loc)

# order the variables


def wmo_square_form(a, b):
    if a < b:
        return [a, b]
    elif a > b:
        return [b, a]


def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
    # normalize the data with the outer function
    # first = wmo_square_form(lat1, lon1)
    # second = wmo_square_form(lon1, lon2)
    first = wmo_square_form(lat1, lat2)
    second = wmo_square_form(lon1, lon2)

    # within will hold the cities that fall within the specified region

    # within is a list comprehension
    # Ensure that the lat and lon valuse are all floats
    # changed values in str function

    # Go through each city and check to see if it falls within
    # the specified coordinates.
    within = [loca for loca in cities if loca.lat > first[0] and loca.lat <
              first[1] and loca.lon > second[0] and loca.lon < second[1]]
    # within = []

    # for city in cities:
    #     if (first_lat > second_lat and first_lon < second_lon):
    #         if(second_lat <= city.lat <= first_lat and second_lon <= city.lon <= first_lon):
    #             within.append(city)
    #     elif (first_lat > second_lat and first_lon < second_lon):
    #         if(second_lat <= city.lat <= first_lat and first_lon <= city.lon <= second_lon):
    #             within.append(city)
    #     elif (first_lat < second_lat and first_lon > second_lon):
    #         if (first_lat <= city.lat <= second_lat and second_lon <= city.lon <= first_lon):
    #             within.append(city)
    #     elif (first_lat < second_lat and first_lon < second_lon):
    #         if (first_lat <= city.lat <= second_lat and first_lon <= city.lon <= second_lon):
    #             within.append(city)

    return within


# within = cityreader_stretch(float(first_lat), float(
#     first_lon), float(second_lat), float(second_lon))
# print the function by iterating over the boxed variables
print(cityreader_stretch(box[0], box[1], box[2], box[3]))

# for city in within:
#     print(city.name, float(city.lat), float(city.lon))
