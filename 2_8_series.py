# In this script, we go through lesson 2.8 of Python Pandas for your
# Grandpa course: Series View vs Copy. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-series-view-vs-copy/

# %% Import libraries
import pandas as pd

# %% View and copy
# Let's define a Series and assign its value to another variable:
x = pd.Series(
    data=[2, 3, 5, 7, 11, 13],
    index=[2, 11, 12, 30, 30, 51]
)
y = x
# Let's modify a value of y:
y.iloc[0] = 999
# Let's print x:
print(x)
# Surprise! x got modified!!! When you do y = x, python is not creating a copy
# of x and storing it in y, but y is just a reference to x. This is an
# assignement. As some people say, y is a view of x.
# If you want to avoid this, use .copy method:
y = x.copy()
y.iloc[1] = -333
print(x)
# x has not been modified. Now y is not making reference to x, but is an
# independent variable.
# This is confusing because assignement by reference only happens some times
# and is not well documented. E.g., we define a Series:
foo = pd.Series(['a', 'b', 'c', 'd'])
# we set bar as:
bar = foo.loc[foo <= 'b']
# and we modify bar:
bar.iloc[0] = 'z'
print(foo)
# foo has not been modified. It means that, when we defined bar, there was some
# underlying process where foo was copied.
# Let's see another example:
baz = foo.iloc[:2]
baz.iloc[0] = 'z'
print(foo)
# But now it was modified, even if bar and baz are (or seem to be) identical...
# When working with Series, normally .loc[] returns a copy and otherwise returns
# a view. However, this is not necessarily always like this and it changes when
# working with data frames. Therefore, it is recommendable to use .copy() if
# we want to avoid this behaviour.

# All this stuff is also relevant for some methods. For instance, the method
# replace:
foo.replace({'a': 'q', 'd': 'p'})
# is creating a copy of foo, so the result is not stored in foo.
# We can assign the value simply by asssigning foo.replace(...) to foo as
# foo = foo.replace(...). But this is inefficient, since pandas is creating
# a new Series, it reassigns this Series to another one, and finally delete
# the old one. Because of this, some pandas methods have the inplace argument,
# which is as if we were creating a view instead of doing .copy:
foo.replace({'a': 'q', 'd': 'p'}, inplace=True)
print(foo)
