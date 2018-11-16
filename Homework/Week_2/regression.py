# Jacob Vermeule 11328622
# Minor Programmeren 2018
# University of Amsterdam


import csv
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets, linear_model
# open csv
input = pd.read_csv("Homework/Week_2/input.csv")

# fill empty spaces
new_csv = input.fillna('100')


# columns which might have a correlation
infant_mortality = new_csv.Infant_mortality
birthrate = new_csv.Birthrate

# make dict of columns
dict = {'infant_mortality': infant_mortality, 'birthrate': birthrate}

# make adjustments to the data
df = pd.DataFrame(data=dict)
df['birthrate'] = df.birthrate.str.replace(',','.').astype(float)
df['infant_mortality'] = df.infant_mortality.str.replace(',','.').astype(float)

# style of plot
plt.style.use('classic')

# length of columns
length = 227

# take values of columns
x = df['infant_mortality'].values
y = df['birthrate'].values

# reshape them to linear regression format
x = x.reshape(length, 1)
y = y.reshape(length, 1)

# fit columns
regr = linear_model.LinearRegression()
regr.fit(x, y)

# make plot
plt.scatter(x, y,  color='red')
plt.plot(x, regr.predict(x), color='blue', linewidth=3)
plt.title('Regression between infant mortality and birthrate')
plt.xticks(())
plt.yticks(())
plt.show()

if __name__ == "__main__":
    plt.show()
