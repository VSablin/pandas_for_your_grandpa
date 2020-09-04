# In this script, we go through lesson 2.2 of Python Pandas for your
# Grandpa course: Series Basic Operations. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-series-basic-operations/

# %% Import pandas and numpy
import numpy as np
import pandas as pd

# %% Sum of a Series and a number
x = pd.Series([1, 2, 3, 4])
x + 1
# The number is added to each element of the Series. However:
x + pd.Series(1)
# Just the first element is a number, the others are NaN. Also, notice that
# the dtype is float64; this is because an integer cannot be NaN, so the first
# element was coerced to float.
# These Nan's appear because, in the second operation, a one-element Series
# is created whose only index is 0. Besides, x is a 4-element Series with
# different indices. The point is that when summing Series just the elements
# with the same indices are summed. The same applies to the other arithmetic
# operations. Let's illustrate this with the following examples:

# %% Sum of two Series
a = pd.Series([10, 20, 30, 40, 50])
b = pd.Series([1, 2, 3, 4, 5])
a + b
# It seems that it is the typical element-wise sum. However:
a.index = np.array([4, 3, 2, 1, 0])
a + b
# Actually is summing elements with the same index.
# If, at some point, you want to make an element-wise operation, you can just
# transform to np arrays:
a.to_numpy() + b.to_numpy()
# And if you want a Series, you can transform back:
pd.Series(a.to_numpy() + b.to_numpy())

# %% Sum of a Series and a np array
a + b.to_numpy()
# As seen, when adding Series and np arrays, the operation is again
# element-wise.
