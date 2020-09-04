# In this script, we go through lesson 2.3 of Python Pandas for your
# Grandpa course: Series Apply. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-series-apply/

# %% Import libraries
import numpy as np
import pandas as pd
import timeit

# %% apply method
# Let's consider a more or less complicated function such as:


def my_func(x):
    return x - 1 if x < 1.5 else x + 1


# and we want to apply this function to each element of a Series:
foo = pd.Series([1.3, 1.9, 1.2, 1.0, 1.7, 1.3])
# Instead of using loops, there is an apply method:
foo.apply(my_func)
# What if the function has arguments?


def my_func_with_params(x, s=1.5, a=1):
    return x - a if x < s else x + a


# We can pass the arguments to apply:
foo.apply(my_func_with_params, s=1.1, a=10)

# %% Performance of apply

# create a huge Series
bigfoo = pd.Series(np.random.uniform(low=1, high=2, size=10000000))
# apply my_func and compute time:
timeit.timeit(lambda: bigfoo.apply(my_func), number=1)
# 2 seconds. Not great.

# For huge Series, it is better to transform first to numpy arrays:


def my_numpy_func(x):
    a = x.to_numpy()
    return np.where(a < 1.5, a - 1, a + 1)


timeit.timeit(lambda: my_numpy_func(bigfoo), number=10)
# 1 second. Not bad. This is because numpy operations actually happen in C,
# whereas pd.Series.apply() are fully-python computations.
