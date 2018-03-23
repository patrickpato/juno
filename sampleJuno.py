# -*- coding: utf-8 -*-
"""
Created on Fri Mar 23 20:42:44 2018

@author: Webster
"""

# A simple program explaining the orbiting of the juno spacecracft over Jupiter. 
orbits = []
for orbit_number in range(0, 50):
    new_orbit = {"speed":148800 , "distancefromatmosphere":4200, "freq": 1000}
    orbits.append(new_orbit)
# Lets assume that for the first 16 orbits, the spaceship has to be closer to the atmosphere of Jupiter to produce more clear images. additionally, the frequency of the signals was increased to give more details. 
#the speed was reduced to provide more time for exploration. 
    for orbit in orbits[0:16]:
        if orbit["speed"] == 148800:
            orbit["speed"] = 74400
            orbit["freq"] = 10000
for orbit in orbits[0:30]:
    print(orbit)
print("...")
print("The total number of revolutions made:" + str(len(orbits)))

# Juno can therefore rest in peace.         