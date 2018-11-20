# Jacob Vermeule 11328622
# Minor Programmeren 2018
# University of Amsterdam
# kijk alles is even lang

import csv
import json


# Open the CSV
f = open('Homework\Week_3\KNMI.csv', 'r')

# Change column names
reader = csv.DictReader(f, fieldnames = ("Station","Date","Temperature"))

# Parse the CSV into JSON
out = json.dumps([row for row in reader])

# Save the JSON
f = open('Homework\Week_3\KNMI.json', 'w')
f.write(out)
