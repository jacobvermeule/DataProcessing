# Jacob Vermeule 11328622
# Minor Programmeren Y2018
# University of Amsterdam

import csv
import json


# Open the CSV
f = open('Homework/Week_6/world_pop.csv', 'r')

# Change column names
reader = csv.DictReader(f, fieldnames = ("Country_Name","id","Indicator_Name","Indicator_Code","Y1960","Y1961","Y1962","Y1963","Y1964","Y1965","Y1966","Y1967","Y1968","Y1969","Y1970","Y1971","Y1972","Y1973","Y1974","Y1975","Y1976","Y1977","Y1978","Y1979","Y1980","Y1981","Y1982","Y1983","Y1984","Y1985","Y1986","Y1987","Y1988","Y1989","Y1990","Y1991","Y1992","Y1993","Y1994","Y1995","Y1996","Y1997","Y1998","Y1999","Y2000","Y2001","Y2002","Y2003","Y2004","Y2005","Y2006","Y2007","Y2008","Y2009","Y2010","Y2011","Y2012","Y2013","Y2014","Y2015","Y2016","Y2017",
))

# Parse the CSV into JSON
out = json.dumps([row for row in reader])

# Save the JSON
f = open('Homework/Week_6/world_pop.json', 'w')
f.write(out)
