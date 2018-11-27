# Jacob Vermeule 11328622
# Minor Programmeren 2018
# University of Amsterdam

import csv
import json


# Open the CSV
f = open('Homework/Week_4/renewable.csv', 'r')

# Change column names
reader = csv.DictReader(f, fieldnames = ('Location','Year','Value'))

# Parse the CSV into JSON
out = json.dumps([row for row in reader])

# Save the JSON
f = open('Homework/Week_4/renewable.json', 'w')
f.write(out)
