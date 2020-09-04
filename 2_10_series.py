# In this script, we go through lesson 2.10 of Python Pandas for your
# Grandpa course: Series Challenges. Web link here:
# https://www.gormanalysis.com/blog/python-pandas-for-your-grandpa-series-challenges/

# %% Import libraries
import numpy as np
import pandas as pd

# %% Strings
# Given a Series of strings, count how many times these words
# occur: {football, shoe, dog}:
strings = pd.Series(['cat', 'shoe', 'car', 'dog', np.nan, 'football', 'shoe',
                     'football', 'cat'])
# Solution:
strings.value_counts().loc[['football', 'shoe', 'dog']]
# .value_counts() is a powerful methods for Series: It gives another Series
# whose indices are the elements of the original Series and the values are
# the number of times each element appears in the original Series.

# %% Missing values
# Given two Series of the same length, A and B, if the ith element
# of B is NaN, double the ith value of A.
A = pd.Series([5, 20, 10, 3, 100, 2], index=[0, 2, 3, 1, 4, 5])
B = pd.Series(data=[True, np.nan, False, np.nan, np.nan, False],
              index=[5, 2, 4, 1, 0, 3])
# Solution:
A.loc[pd.isna(B).to_numpy()] *= 2
print(A)

# %% Comparing Series
# Given a Series of car asking prices and another of car fair
# prices, determine which cars are a good buy. The result must be a list of
# integer indices corresponding to the good buys in the Series with asking
# prices.
asking_prices = pd.Series(data=[5000, 7500, 9000, 8500, 7000],
                          index=['escape', 'escape', 'ranger', 'mustang',
                                 'mustang'])
fair_prices = pd.Series(data=[5500, 7500, 7500],
                        index=['escape', 'mustang', 'ranger'])
# Solution:
c = 'escape'
bool = (asking_prices <= fair_prices.loc[c]).to_numpy() & \
 (asking_prices.index == c)
int_escape = np.where(bool)

c = 'mustang'
bool = (asking_prices <= fair_prices.loc[c]).to_numpy() & \
 (asking_prices.index == c)
int_mustang = np.where(bool)

c = 'ranger'
bool = (asking_prices <= fair_prices.loc[c]).to_numpy() & \
 (asking_prices.index == c)
int_ranger = np.where(bool)

sol = np.concatenate([int_escape[0], int_mustang[0], int_ranger[0]]).tolist()
print(sol)
asking_prices.iloc[sol]
asking_prices.index
# The solution proposed by gormanalysis is pretty different. Go to the link
# (see header) to know more.

# %% Stocks
# Given a Series of stock prices at times 0, 1, 2... determine which had the
# greatest price increase from the day before.
np.random.seed(123)
stock_prices = pd.Series(data=np.random.uniform(low=100, high=200, size=10),
                         index=np.random.choice(np.arange(10), size=10,
                                                replace=False))
gap = 0
day = 0
for i in np.arange(1, 10):
    new_gap = stock_prices.loc[i] - stock_prices.loc[i-1]
    if new_gap > gap:
        gap = new_gap
        day = i

print(day)
# gormanalysis, again, proposes a different solution. This time I'll reproduce
# this alternative here, since they use pretty handy methods:

# Step 1: Sort stock_prices by its index via .sort_index():
stock_prices.sort_index(inplace=True)
# Step 2: Create a new Series with the previous day's prices using .shift():
stock_prices_prev = stock_prices.shift(periods=1)
# Step 3: Calculate the day-to-day gap:
daily_changes = stock_prices - stock_prices_prev
# Step 4: Find the index corresponding the the maximum value of daily_changes
# with .idxmax()
daily_changes.idxmax()
