"""
-------------------------------------------------------
[Lab 2, Task 7]
-------------------------------------------------------
Author:  Usama Mohiuddin
ID:      212090340
Email:   mohi0340@mylaurier.ca
__updated__ = "2021-09-21"
-------------------------------------------------------
"""
# input values
numflyers = int(input("Number of Flyers:"))
numvolunteers = int(input("Number of Volunteers:"))

# number of flyers per volunteer
flyersper = numflyers // numvolunteers

print(
    "The Number of Flyers Per Volunteer:", flyersper)

# left over flyers calculation using (%)
leftover = numflyers % numvolunteers

print(
    "Flyers Left Over:", leftover)
