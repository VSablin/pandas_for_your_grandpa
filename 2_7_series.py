# In this script, we go through lesson 2.7 of Python Pandas for your
# Grandpa course: Series Boolean Indexing. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-series-boolean-indexing/

# %% Import libraries
import pandas as pd

# %% Boolean Indexing:
# Just like np arrays, Series can be indexed with boolean variables:
foo = pd.Series([20, 50, 11, 45, 17, 31])
# We first define a boolean Series with some condition:
lt20 = foo < 20
lt20
# We then can subset foo with lt20 via loc:
foo.loc[lt20]
# Or, more straightforwardly:
foo.loc[foo < 20]
# Let's now play with indices:
foo.index = [0, 1, 2, 3, 5, 4]
foo.loc[lt20]
# So we see here that what actually Series.loc[boolean_Series] is comparing
# the indices of both Series and then keeps those elements of the initial
# Series such that the boolean is equal to True.
# If, at some point, you are not interested in the indices, go to np:
foo.loc[lt20.to_numpy()]

# %% Combining boolean Series
# It is possible to combine several boolean conditions:
# AND (&):
foo.loc[(foo < 40) & (foo > 20)]
# OR (|):
foo.loc[(foo < 40) | (foo > 20)]
# NEGATION (~):
foo.loc[~(foo % 10 == 0)]
# REMARK: Make sure to wrap each condition in parenthesis, otherwise you will
# get errors:
foo.loc[foo > 40 | foo < 20]
