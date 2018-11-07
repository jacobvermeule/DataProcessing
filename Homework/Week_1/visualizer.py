#!/usr/bin/env python
# Name: Jacob Vermeule
# Student number: 11328622
# to get a correct list of the years i had to delete the comma in the title
# of movie number 47 in the csv.
"""
This script visualizes data obtained from a .csv file
"""

import csv
import matplotlib.pyplot as plt

# Global constants for the input file, first and last year
INPUT_CSV = "movies.csv"
START_YEAR = 2008
END_YEAR = 2018

# open csv file
with open("movies.csv", 'r') as csvfile:
    movies = csv.reader(csvfile, quotechar = '|')

    # create empty lists for each years movie ratings
    first = []
    second = []
    third = []
    fourth = []
    fifth = []
    sixth = []
    seventh = []
    eigth = []
    nineth = []
    tenth = []

    # extract rating of every year
    for rows in movies:
        if rows[2] == '  2008':
            first.append(float(rows[1]))
        if rows[2] == '  2009':
            second.append(float(rows[1]))
        if rows[2] == '  2010':
            third.append(float(rows[1]))
        if rows[2] == '  2011':
            fourth.append(float(rows[1]))
        if rows[2] == '  2012':
            fifth.append(float(rows[1]))
        if rows[2] == '  2013':
            sixth.append(float(rows[1]))
        if rows[2] == '  2014':
            seventh.append(float(rows[1]))
        if rows[2] == '  2015':
            eigth.append(float(rows[1]))
        if rows[2] == '  2016':
            nineth.append(float(rows[1]))
        if rows[2] == '  2017':
            tenth.append(float(rows[1]))

# average rating per year
average = []

average2008 = average.append(sum(first) / len(first))
average2009 = average.append(round((sum(second) / len(second)), 2))
average2010 = average.append(round((sum(third) / len(third)), 2))
average2011 = average.append(round((sum(fourth) / len(fourth)), 2))
average2012 = average.append(round((sum(fifth) / len(fifth)), 2))
average2013 = average.append(round((sum(sixth) / len(sixth)), 2))
average2014 = average.append(round((sum(seventh) / len(seventh)), 2))
average2015 = average.append(round((sum(eigth) / len(eigth)), 2))
average2016 = average.append(round((sum(nineth) / len(nineth)), 2))
average2017 = average.append(round((sum(tenth) / len(tenth)), 2))

years = []
for i in range(START_YEAR, END_YEAR):
    years.append(i)

# Global dictionary for the data
data_dict = dict(zip(years, average))
plt.style.use('dark_background')
plt.title('Average rating of top 50 movies from 2008-2017', fontsize=12, fontweight='bold')
plt.plot(years, average, 'w', label='line through averages')
plt.plot(years, average, 'ro', label='average point')
plt.xlabel("Year of release")
plt.ylabel("Average rating on a scale of 1 to 10")
plt.legend(frameon = True)
plt.axis([2008, 2017, 8, 9])
plt.show()
