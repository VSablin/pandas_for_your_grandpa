# In this script, we go through lesson 2.6 of Python Pandas for your
# Grandpa course: Series Concatenation. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-series-concatenation/

# %% Import libraries
import numpy as np
import pandas as pd

# %% Index type
# We first define a few Series:
rg_idx = pd.Series([1, 2, 3, 4])
int_idx = pd.Series([10, 20, 30, 40], index=[0, 1, 2, 3])
float_idx = pd.Series([5, 10, 15, 20], index=[0., 1., 2., 3.])
string_idx = pd.Series([11, 22, 33, 44], index=['0', '1', '2', '3'])
# We can concatenate Series with pd.concat.
# RangeIndex + int index:
a = pd.concat(objs=(rg_idx, int_idx))
a
a.index
# RangeIndex + int index + float index:
b = pd.concat(objs=(rg_idx, int_idx, float_idx))
b
b.index
# RangeIndex + int index + float index + string index:
c = pd.concat(objs=(rg_idx, int_idx, float_idx, string_idx))
c
c.index
# The rule is that, when you concatenate Series with different types of index,
# the index are coerced to the highest level data type, being the hierarchy:
# range < int < float < string/object

# %% Element type
# The same applies to the element types:
int_vals = pd.Series([10, 20, 30, 40])
float_vals = pd.Series([10., 20., 30., 40.])
string_vals = pd.Series(['100', '200', '300', '400'])

x = pd.concat((int_vals, float_vals))
x.dtype
y = pd.concat((int_vals, float_vals, string_vals))
y.dtype
