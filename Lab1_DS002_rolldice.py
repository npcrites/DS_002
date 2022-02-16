from collections import Counter
import seaborn as sns

# Plotting cell
from matplotlib import pyplot as plt

# font
plt.rcParams.update({'font.size': 8})

# reset the default figsize value
plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]

# 144 is good for a high-resolution display. Try 100 if it's too big
plt.rcParams["figure.dpi"] = (120)

from random import randint, seed
seed()

import statistics as stats

def rollDie(sides=6):
    return randint(1,sides)

def rollDice(howmany=2):
  """Roll howmany fair die"""
  r = []
  for i in range(howmany):
    r.append(rollDie())
  return stats.mean(r)

def rollDieNtimes(n=50):
  """Roll one die n times"""
  ppg = []
  for _ in range(n):
    ppg.append(rollDie())
  return ppg

def rollDiceNtimes(n=50):
  """Roll two dice n times"""
  ppg = []
  for _ in range(n):
    ppg.append(rollDice())
  return ppg

def getMean (alist = [1,6]):
    return stats.mean(alist)

rollDie(), rollDice(), rollDice(3), rollDice(30), rollDieNtimes(10), rollDiceNtimes(10)

aYear = rollDieNtimes(n=36500)
# Sanity check
stats.mean(aYear), stats.median(aYear)

from collections import Counter

# Proper Currency formatting
import locale
locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

freq = Counter(aYear)

print("| $gal | sales |")
print("|------|-------|")
for k in sorted(freq.keys()):
  print(f"| ${k}   | {freq[k]}  |")

print()
print(f"Mean price is ${stats.mean(aYear)}/gal")
print(f"Median price is ${stats.median(aYear)}/gal")

totalSales = 0
for k in freq.keys():
  totalSales = totalSales + (k * freq[k])

print(f"Total sales for the year: {locale.currency(totalSales, grouping=True)}")


import seaborn as sns
keys = sorted(dict(freq).keys())

vals = []
for k in keys:
  vals.append(dict(freq)[k])


# x = [d for d in range(len(aYear))]
sns.barplot(x=keys,y=vals)
plt.title("Distribution of customers and prices paid")
plt.show()

# use rollDiceNtimes to simulate a year of sales
aYear = [
    [1,3],[4,3],[4,2],[1,1],[5,5],[6,5],[2,2],[5,2],[6,5],[5,2],[6,4],[3,2],[2,1],[6,4],[3,2],[5,4],[2,4],[5,3],[1,1],[4,6],[4,3],[4,6],[1,3],[4,5],[2,5],[6,1],[5,4],[4,5],[2,1],[2,1],[4,1],[1,2],[3,1],[5,4]
    ]
# Your mean should be close to 3.5

#mean

findMean = []

for i in aYear:
    findMean.append(stats.mean(i))
print(sum(findMean)/len(findMean))

#median

stats.median(findMean)

# Output will look like this:
# (3.5048356164383563, 3.5)

# Create a dictionary called freq to count the frequency of each price paid

freq = Counter(findMean)

print("| $gal   | sales |")
print("|--------|-------|")
for k in sorted(freq.keys()):
  print(f"| ${k}   | {freq[k]}  |")

print()
print(f"Mean price is ${stats.mean(findMean)}/gal")
print(f"Median price is ${stats.median(findMean)}/gal")

# Calculate the total sales
sales = []
for key in freq.keys():
    val = freq[key]
    x = key*val
    sales.append(x)
totalSales = sum(sales)


#totalSales = freq.keys()*freq.values()


print(f"Total sales for the year: {locale.currency(totalSales, grouping=True)}")


# Your output will look like this:

# | $gal   | sales |
# |--------|-------|
# | $1.0   | 1003  |
# | $1.5   | 2003  |
# | $2.0   | 3022  |
# | $2.5   | 3949  |
# | $3.0   | 5117  |
# | $3.5   | 6198  |
# | $4.0   | 5051  |
# | $4.5   | 4121  |
# | $5.0   | 3002  |
# | $5.5   | 2008  |
# | $6.0   | 1026  |

# Mean price is $3.5048356164383563/gal
# Median price is $3.5/gal
# Total sales for the year: $127,926.50

# Get a list of keys from the freq dictionary
# NOTE: you will need to sort the keys!
sortedFreqkeys = sorted(freq.keys())
sortedVals = []
for key in sortedFreqkeys:
    val = freq[key]
    sortedVals.append(val)
print(f"The keys are: {sortedFreqkeys}\nThe associated values are: {sortedVals}")
    
    
# Get a list of corresponding values from the freq dictionary


# Make a plot. Does it have the same shape as the 1-Die? plot?
sns.barplot(x=keys,y=vals)
plt.title("Number of customers over price paid per gallon")
plt.show()

import random
# This is a simulation -- use the die, try your luck!
twoYears = []
for i in range(0,100):
    n = random.randint(1,6)
    twoYears.append(n)
print(twoYears)

# stats.mean(aYear), stats.median(aYear)

paid = []
avg = []
totalcost = 0
for p in twoYears:
  totalcost = totalcost+(p*10)
  paid.append(p)
  avg.append(stats.mean(paid))

sns.lineplot(y=avg,x=[r for r in range(len(avg))])
plt.ylim(1, 6)
plt.title(f"Total Lucky 1-Die cost over 100 fill ups: {totalcost}")
plt.show()

import numpy as np
myrolls = []

for i in range(0,100):
    randnums= np.random.randint(1,6,2)
    myrolls.append(randnums)
    
twoYearsDice = []

for r in myrolls:
  twoYearsDice.append(getMean(r))

print(f"The mean of the two dice from each roll: \n{twoYearsDice}")

paid = []
avg = []
totalcost = 0
for p in twoYearsDice:
  totalcost = totalcost+(p*10)
  paid.append(p)
  avg.append(stats.mean(paid))

sns.lineplot(y=avg,x=[r for r in range(len(avg))])
plt.ylim(1, 6)
plt.title(f"Total Lucky 2-Dice Gas cost over 100 fill ups: {totalcost}")
plt.show()
