# In this script, we go through lesson 2.9 of Python Pandas for your
# Grandpa course: Series Missing Values. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-series-missing-values/

# %% Import libraries
import numpy as np
import pandas as pd

# %% Series with integers
# Let's define a Series
roux = pd.Series([1, 2, 3])
# and introduce a NaN value:
roux.iloc[1] = np.nan
print(roux)
# We have properly introduced a missing value (NaN), but the dtype has been
# coerced to float. To avoid this we can use dtype argument when creating the
# Series:
roux = pd.Series([1, 2, 3], dtype='Int64')
roux.iloc[1] = np.nan
print(roux)
# There are two alternatives (probably better):
roux.iloc[1] = None
print(roux)
roux.iloc[1] = pd.NA
print(roux)

# %% Series with strings
# Let's define a Series with strings and set a couple of values to None and
# np.nan:
gumbo = pd.Series(['a', 'b', 'c'])
gumbo.iloc[1] = None
gumbo.iloc[2] = np.nan
print(gumbo)
# As seen, the format is "Object", because the Series contains elements with
# different types. To avoid this (and keep the type of the original Series):
gumbo = pd.Series(['a', 'b', 'c'], dtype='string')
gumbo.iloc[1] = None
gumbo.iloc[2] = np.nan
print(gumbo)
# Now the format is "string" *AND* both None and np.nan are coerced to "<NA>".

# %% Subsetting missing values
# Given a Series x, it is not possible to subset the missing values with via
# x == np.nan, since np.nan == np.nan gives False:
x = pd.Series([1.0, np.nan, 3.0, np.nan])
x == np.nan
# To find nan's we have the function pd.isna(); if you want to find NOT_nans,
# there exists pd.notna():
pd.isna(x)
pd.notna(x)
# We can replace NaN values via .loc and pd.isna():
x.loc[pd.isna(x)] = -1
print(x)
# Alternatively, you can use the .fillna method:
x = pd.Series([1.0, np.nan, 3.0, np.nan])
x.fillna(-1)
# This does not change x, but it generates a copy. To modify x:
x.fillna(-1, inplace=True)
print(x)
