# Jacob Vermeule 11328622
# Minor Programmeren 2018
# University of Amsterdam


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import json

# open csv
input = pd.read_csv("Homework/Week_2/input.csv")

# fill empty spaces
new_csv = input.fillna('NaN')

# extract required columns
country = new_csv.Country
region = new_csv.Region
pop_density = new_csv.Pop_Density
infant_mortality = new_csv.Infant_mortality
gdp = new_csv.GDP

# make dictionary of columns
dict = {'Country':country, 'region': region, 'population_density': pop_density,
        'infant_mortality': infant_mortality, 'GDP': gdp}

# make adjustments to the data
df = pd.DataFrame(data=dict)
df['GDP'] = df.GDP.str.replace("dollars",'').astype(float)
df['population_density'] = df.population_density.str.replace(',','.').astype(float)
df['infant_mortality'] = df.infant_mortality.str.replace(',','.').astype(float)

# get values of GDP
mean = df['GDP'].mean()
median = df['GDP'].median()
mode = df['GDP'].mode()
standard_deviation = df['GDP'].std()

# take out the outliers
dfgdp = df[np.abs(df.GDP-df.GDP.mean()) <= (3*df.GDP.std())]
plt.style.use('classic')

# initiate two plots
fig, axes = plt.subplots(nrows=1, ncols=2)

# make histogram
dfgdp.GDP.hist(ax=axes[0], bins=50, xlabelsize=10, ylabelsize=10, facecolor='b', rwidth=0.8)
axes[0].set_title('Average GDP per country')
axes[0].set_xlabel('GDP in $')
axes[0].set_ylabel('Frequency')

# calculate five number summary
minimum = df['infant_mortality'].min()
First_Quantile = df['infant_mortality'].quantile(q=0.25)
median_of_infant_mortality = df['infant_mortality'].median()
Third_Quantile = df['infant_mortality'].quantile(q=0.75)
maximum =  df['infant_mortality'].max()


# make boxplot
df.boxplot(column='infant_mortality',ax=axes[1], )
axes[1].set_title('Infant deaths per 1000 births per country')
axes[1].set_ylabel('Number of deaths')

# write data to json file
df = df.set_index('Country')
dfjson = df.to_json(orient='index')

# save jsonfile locally
with open('dfjson.json', 'w') as outfile:
    json.dump(dfjson, outfile)

if __name__ == "__main__":
    plt.show()
