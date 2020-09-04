# In this script, we go through lesson 2.3 of Python Pandas for your
# Grandpa course: Series Basic Indexing. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-series-basic-indexing/

# %% Import libraries
import numpy as np
import pandas as pd
import sys

# %% Accessing Series elements
x = pd.Series([5, 10, 15, 20, 25])
# In order to access each element, we use the typical bracket notation,
# but the number in the bracket makes reference to the index of the element.
# So, x[0] returns the element with index 0, x[1] the element with index 1, etc.
# Let us illustrate this by reordering the indices:
x.index = np.array([3, 1, 4, 0, 2])
x[0]
# It is not 5, but 20.
# It is still possible to access the i-th element of the Series (instead of
# the element with index i) via iloc:
x.iloc[0]
x.iloc[1]
# Negative indexing is allowed:
x.iloc[-2]
# slicing:
x.iloc[1:4:2]
# or even pass a list, array, or Series of indices:
x.iloc[[0, 2, 3]]
x.iloc[np.array([0, 2, 3])]
x.iloc[pd.Series([0, 2, 3])]

# %% Index
# As seen, when we define a Series, it automatically gets an index of sequential
# values starting from 0:
grades = pd.Series([82, 94, 77, 89, 91, 54])
print(grades)
# We can modify the index by assigning a list, array, or Series with the proper
# length via the .index method. Notice that they don't need to be integers:
grades.index = ['john', 'ray', 'sue', 'ben', 'kellie', 'ed']
print(grades)
# And now we can know Sue's grade:
grades['sue']
# This is one of the advantages of indices: You don't have to remember the order
# Another nice feature is that arithmetic operations with Series compare the
# value of the indices. Therefore, if we have a second Series grades2 with the
# same values for the indices ('john', 'ray', etc.) and want to add both Series,
# we do not need to make sure that both are ordered in the same way, we just
# need the indices to be the same (even if they have different ordering). Let
# us see this and how to define a series with nontrivial indices:
grades2 = pd.Series(
    data=[91, 90, 79, 83, 98, 90],
    index=['ray', 'ed', 'ben', 'kellie', 'sue', 'john']
)
(grades + grades2)/2
# Also, when indices are integers, x[0] gives the element with index 0 of
# the Series x. However, when indices are not integers (typically strings),
# you get the first element. For instance:
grades[0]
# This can be confusing, so this bracket notation is not recommended. Instead,
# try using .iloc for elements and .loc for indices:
grades.loc['john']
# slicing is also allowed:
grades.loc['sue':'kellie']
# Contrarily to slicing with .iloc, here the right boundary is included.
# Lists, arrays, and Series can also be used with .loc:
grades.loc[['ray', 'john', 'ben']]
grades.loc[np.array(['ray', 'john', 'ben'])]
grades.loc[pd.Series(['ray', 'john', 'ben'])]

# %% Index types
# We have seen that, when defining a Series from scratch, it automatically
# assigns a sequence to the indices. In particular, RangeIndex:
x = pd.Series(np.random.normal(size=10**7))
x.index
# This is not fully equivalent to:
y = pd.Series(np.random.normal(size=10**7), index=np.arange(10**7))
y.index
# From a high-level perspective, x and y are pretty much the same. The main
# difference is that the first option does not need to store 10**7 numbers
# for the indices, but just a RangeIndex object. Let's see this:
sys.getsizeof(x)
sys.getsizeof(y)
# The size of y is about twice that of x.
# Another advantage of RangeIndex: It is more efficient to find elements.
# Finally, the advantage of int or string indices is that two elements of the
# Series or more can have the same index, which can be useful. E.g.:
foo = pd.Series([2, 3, 5, 7, 11], index=[0, 0, 1, 1, 2])
foo.loc[0]
foo.loc[1]
foo.loc[2]
