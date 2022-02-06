##Nick Crites HW1 DS_002

from collections import Counter, OrderedDict
import seaborn as sns



# Set your username here
# This will be the name of the local repository folder/directory
USERNAME = "npcrites"

# Plotting cell
from matplotlib import pyplot as plt

# font
plt.rcParams.update({'font.size': 8})

# reset the default figsize value
plt.rcParams["figure.figsize"] = plt.rcParamsDefault["figure.figsize"]

# 144 is good for a high-resolution display. Try 100 if it's too big
plt.rcParams["figure.dpi"] = (100)



# Import your code from GitHub

# This is the root on Google Colab
# Use the magic %cd command to navigate around the file system
%cd /content/

# Use `isdir()` to see if the repository is already here
from genericpath import isdir

# get your code
# Does the folder/directory exist?

# Clone the repository with the latest code
print("Clone the repo")
!git clone https://github.com/scrippscollege/DS_002.git npcrites

%cd /content/npcrites
!git pull

%cd /content/



# now you can import introduction.py
# IMPORTANT: Add your foldername here:
# from dgoodwin import introduction as intro
#from npcrites import introduction as intro

# What's in introduction ?
#dir(intro)

# need some help?
#help(intro)


###Start HW1

noirdata = [['2/1/2022 22:16:08', 'Dirty blonde', 'Like', '26', '2766'],
 ['2/1/2022 22:18:05', 'Brown', 'Love', '50', '14'],
 ['2/2/2022 0:39:29', 'Black', 'Like', '18', '1012'],
 ['2/2/2022 8:53:33', 'Black', 'Love', '75', '8346'],
 ['2/2/2022 9:57:23', 'Brown', 'Like', '45', '2601'],
 ['2/2/2022 10:02:53', 'black', 'Like', '45', '2634'],
 ['2/2/2022 10:19:44', 'dark brown', 'Like', '14', '5965'],
 ['2/2/2022 10:25:07', 'Brown', 'Love', '19', '776'],
 ['2/2/2022 10:26:05', 'Brown', 'Like', '75', '2660'],
 ['2/2/2022 10:51:12', 'blonde', 'Love', '60', '373'],
 ['2/2/2022 10:59:27', 'Brown', 'Like', '33', '2124'],
 ['2/2/2022 11:00:35', 'Black ', 'Like', '61', '25'],
 ['2/2/2022 11:03:29', 'Brown', 'Love', '59', '35'],
 ['2/2/2022 11:03:36', 'brown', 'Love', '62', '45'],
 ['2/2/2022 11:03:59',
  'Blond and brown (in different areas)',
  'Like',
  '46',
  '2664'],
 ['2/2/2022 11:04:04', 'Brown', 'Love', '32', '1003'],
 ['2/2/2022 11:04:11', 'black and blue', 'Like', '59', '374'],
 ['2/2/2022 11:05:19', 'black', 'Like', '43', '1412'],
 ['2/2/2022 11:17:10', 'red', 'Like', '6', '6056']]


#How many different hair colors are there in the class?

emptydict = {}
for row in noirdata:
    j = row[1].lower()
    if j in emptydict:
        emptydict[j] += 1
    else:
        emptydict[j] = 1

        
print(len(emptydict))

#OR

from collections import Counter

# make a list of all the hair colors
allcolors = [row[1] for row in noirdata]

# Make your frequency counter
c = Counter(allcolors)
print (len(c))

print()

#What is the most frequent response or median response about chocolate?

allfeels = [row[2] for row in noirdata]
count = Counter(allfeels)

sort_orders = sorted(count.items(), key=lambda x: x[1], reverse = True)
for i in sort_orders:
    print(i[0], i[1])
    
print ()

#Could you calculate an average or mean response?

from statistics import mean, mode, median, median_grouped

scores = {"Hate": -2, "Tolerate":-1, "Neutral":0, "Like":1, "Love":2}
print(f"The scores are given like this: {scores}")

feelScores = []
for f in allfeels:
    myscore = scores[f]
    feelScores.append(myscore)
print(f"The feelScores list constains {feelScores}")

if (mean(feelScores) < -1.5):
    print("Most people in the class hate chocolate")
elif (mean(feelScores) < -0.5):
    print("Most people in the class tolerate chocolate")
elif (mean(feelScores) < 0.5):
    print("Most people in the class feel neutral about chocolate") 
elif (mean(feelScores) < 1.5):
    print(f"Most people in the class like chocolate since the average is {(mean(feelScores))}")
elif (mean(feelScores) < 2):
    print("Most people in the class tolerate chocolate")

print()

#What is the mean temperature of our hometowns?

alltemps = [int(col[3]) for col in noirdata]
meanTemp = mean(alltemps)
print(f"The mean temperature of our hometowns is: {meanTemp} degrees")

print()

#What is the minumum temperatures of our hometowns?

minTemp = min(alltemps)
print(f"The minimum temperature of the class hometowns is: {minTemp} degrees")

print()

#What is the maximum temperature of our hometowns?

maxTemp = max(alltemps)
print(f"The maximum temperature of the class hometowns is: {maxTemp} degrees")

print()

#What is the average or mean distance to our hometowns?
allDist = [int(col[4]) for col in noirdata]
avgDist = round(mean(allDist))
print(f"The average distance from Claremont to our hometowns is about {avgDist} miles")

print()

#What is the furthest distance?
farAway = max(allDist)
print(f"The furtest hometwn is {farAway} miles away from Claremont")

print()

#What is the closest distance?
veryClose = min (allDist)
print(f"The closest hometown is {veryClose} miles away from Claremont")

print()

#What is the 50th percentile?
print(f"The 50th percentile of data median_grouped is {median_grouped(allDist)} miles")

print()

#making my bar plot showing the distribution of chocolate lovers
chocolate = Counter(allfeels)

keys = list(chocolate.keys())
vals = list(chocolate.values())

theSpread = OrderedDict([
    ('Hate',0),
    ('Tolerate',0),
    ('Neutral',0),
    ('Like', 0),
    ('Love',0),
    ])

for k in chocolate.keys():
    theSpread[k] = chocolate[k]

keys = list(theSpread.keys())
vals = list(theSpread.values())

#seaborn barplot
sns.barplot(x=keys,y=vals).set(title='Do you like chocolate?')
plt.title = "What does this do"
plt.show()
