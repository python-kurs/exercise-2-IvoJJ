# Exercise 2

# Satellites:
sat_database = {"METEOSAT" : 3000,
                "LANDSAT"  : 30,
                "MODIS"    : 500
               }

# The dictionary above contains the names and spatial resolutions of some satellite systems.

# 1) Add the "GOES" and "worldview" satellites with their 2000/0.31m resolution to the dictionary [2P]

sat_database['GOES'] = 2000
sat_database['worldview'] = 0.31

# 2) print out all satellite names contained in the dictionary [2P]

print("I have the following satellites in my database: {}.".format(sat_database.keys()))

# 3) Ask the user to enter the satellite name from which she/he would like to know the resolution [2P]
name = input("Enter the desired Satellite to get the resolution: ")
# 4) Check, if the satellite is in the database and inform the user, if it is not [2P]

if name in sat_database:
    print("Satellite {} is in the dataset and has a resoltuion of {} meters.".format(name,sat_database[name.upper()]))
else:
    print("There is no such satellite {} in the dataset.".format(name))
    
# 5) If the satellite name is in the database, print a meaningful message containing the satellite name and it's resolution [2P] 
#see 4)