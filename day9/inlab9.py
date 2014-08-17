from pandas import Series, DataFrame
import pandas as pd
import numpy as np

# create a data series - basically an array
mySeries = Series([4, 3, 5, np.nan, 6, 8])
print mySeries
mySeries.values
mySeries.index 

mySeries2 = Series([3,5,7,9], index=['d', 'c', 'a', 'b'])
print mySeries2 
mySeries2.values # make them check values
mySeries2.index 

# Series work kind of like lists
mySeries[1]
mySeries2['d']
mySeries[['c', 'a', 'd']]
mySeries2[mySeries2 > 0] # equivalent to which() in R
myDoubled = mySeries * 2 # perform functions on your arrays
np.exp(myDoubled)

# Series indices can be thought of like dicts, but are immutable
'b' in mySeries2
'e' in mySeries2

# We can even turn dicts into series
eVotes = {'NC': 15, 'TX': 38, 'CA': 55} # sorted by key
ev = Series(eVotes)
states = ['CA', 'NC', 'TX', 'OH']
ev2 = Series(ev, states)

# Series have a name, as do their indices
ev2.name = "electoral votes"
ev2.index.name = "state"
print ev2


# DataFrames are fun too 

data = pd.read_csv("http://joshcutler.github.com/PS632-Spring2013/assets/Week9/lab9.csv")
print data.head()
data['State']
# change column names for convenience
data.columns = ['st', 'yr', 'ev', 'pop']

# we can create new columns
data['popm'] = data['pop'] / 1000000.0
data['evs'] = data['ev'] -3
data.head()
del data['evs']
data.head() 

# DataFrames can be indexed 
data[1:4]
data[data['yr']==2010]
data[data['ev']>40]

# TODO: what's the minimum population in 1990? 
# in which state was that? 
# how many states had over 35 electoral votes in 2010? 

# we can also apply functions to columns
format = lambda x: '%.2f' % x 
data['popm'].map(format) 

# sort on values
data2 = data.sort_index(by='popm')
data2.head()
data2.tail()

# summary statistics
# d1990.sum()
data.describe()
data.std()

# how much did total population change between 1990 and 2010? 
# TODO: how many people did the average congressperson represent in 1990?

# we could also represent a single variable as a series with hierarchical indexing
p = Series(data['pop'].values, index=[data['st'], data['yr']])
p['North Carolina']
p.mean(level='st')
# TODO: calculate standard deviation by year

p.swaplevel('st', 'yr')

# correlation
data['pop'].corr(data['ev'])

# estimate a linear model
model = pd.ols(y=data['ev'], x=data['popm'])
print model 
model.beta