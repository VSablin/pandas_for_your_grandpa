# In this script, we go through lesson 2.1 of Python Pandas for your
# Grandpa course: Series Creation. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-Series-creation/

# %% Import pandas
import pandas as pd

# %% Define a Series
x = pd.Series([5, 10, 15, 20, 25])

# %% Print the Series
print(x)
# Notice that the output is not just the set of values and the type of
# variable, but it contains the indices for each element. This is one of the
# differences between pd Series and np arrays.

# Remark: All the elements of a Series shoul have the same type (it is possible
# to combine types, but it is not recommended).

# %% type
type(x)

# If you want to know the type of the elements in a Series:
x.dtype

# %% From pd.Series to np.array:
x.to_numpy()
# .values is also possible, but it is deprecated.
x.values

# %% From pd.Series to dictionary:
# We first define a dictionary
data = {'a': 0., 'b': 1., 'c': 2., 'e': 3.}
# Then transform to pd.Series:
y = pd.Series(data)
print(y)
# As seen in the output, the keys of the dictionary are the indices of the
# Series and the dictionary values are the Series values.

# %% Series from a numpy array
# import numpy
import numpy as np
# define a np array
hw = np.array(['hello', 'world', 'hello', 'world'])
# transform to Series
z = pd.Series(hw)
print(z)
# Notice that the dtype is 'object'. This happens in the particular case of
# string-like arrays, since, actually, the Series has an underlying set of
# pointers pointing to the blocks of memory where the strings are located.
# This happens just with strings and this is due to the fact that the memory
# that a string occupies is variable (contrarily to integers, floats, etc.).

# %% Series from scratch
# One option is creating np arrays and then transform them to pd Series
# Example 1: np.arange for a sequence
sequence = pd.Series(np.arange(start=10, stop=60, step=10))
# Example 2: normally distributed numbers
randnorm = pd.Series(np.random.normal(size=5))
print(randnorm)
