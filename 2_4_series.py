# In this script, we go through lesson 2.4 of Python Pandas for your
# Grandpa course: Series Overwriting Data. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-series-overwriting-data/

# %% Import libraries
import numpy as np
import pandas as pd

# %% Overwriting with iloc
foo = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[10, 40, 50, 30, 20])
# We can use iloc to replace an element:
foo.iloc[1] = 'w'
print(foo)
# replace a set of elements:
foo.iloc[[0, 1, 2]] = 'x'
print(foo)
# or use slicing:
foo.iloc[:3] = 'x'
print(foo)

# %% Overwriting with loc
# We can do the same with loc:
foo = pd.Series(['a', 'b', 'c', 'd', 'e'], index=[10, 40, 50, 30, 20])
foo.loc[40] = 'w'
foo.loc[[10, 40, 50]] = 'x'
foo.loc[10:50] = 'x'

# %% Overwrite all the elements
# Let's assume we want to replace all the elements of foo by
new_vals = np.array([5, 10, 15, 20, 25])
# Doing something like foo = pd.Seris(new_vals) is not a good idea, since the
# indices will be removed. Instead, use slicing:
foo.iloc[:] = new_vals
print(foo)

# %% Overwriting with another Series
x = pd.Series([10, 20, 30, 40])
y = pd.Series([1, 11, 111, 1111], index=[7, 3, 2, 0])
x.loc[[0, 1]] = y
print(x)
# What the last operaton did was to assign y.loc[0] to x.loc[0] and y.loc[1]
# to x.loc[1]. As y.loc[1] does not exist, x.loc[1] is now NaN. Besides, notice
# that the type is now float64.
# We can combine this with slicing:
x.iloc[:2] = y
print(x)
# We can also use numpy arrays, but they must have the same length. Otherwise,
# you get an error:
x.loc[[0, 1]] = y.to_numpy()
# However, this works:
x.loc[[0, 1]] = y.to_numpy()[:2]
print(x)
