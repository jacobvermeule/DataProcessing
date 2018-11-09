import csv
import pandas

country = []
region = []
pop_dens = []
inf_mort = []
gdp = []
# open csv
with open("Homework/Week_2/input.csv", 'r') as csvfile:
    input = csv.reader(csvfile, quotechar = '|')
    next(input)
    next(input)
    for rows in input:
        if rows != ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '']:
            for i in rows:
                i.replace('', 'unknown')
            # append countries to list
            countries = rows[0]
            country.append(countries)

            # append regions to list
            regions = rows[1]
            region.append(regions)


            pop_density = rows[4]
            pop_dens.append(pop_density)


            infant_mortality = rows[7]
            inf_mort.append(infant_mortality)

            gdps = rows[8]
            gdp.append(gdp)


print(inf_mort)
