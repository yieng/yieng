# Assumption: only mp3 files, folders and hidden files are in the directory /path.

import os

# The folder containing files.
D0 = "/path/"

# Get all files.
L0 = os.listdir(D0)

# Loop and add files to list.
pairs = []
for file in L0:

    # Use join to get full file path.
    location = os.path.join(D0, file)

    # Get size and add to list of tuples.
    size = os.path.getsize(location)
    pairs.append((size, file))

# Sort list of tuples by the first element, size.
pairs.sort(key=lambda s: s[0])

# Display pairs.
n = 0
##for pair in pairs:
##    print(n, pair)
##    n += 1

pairs = pairs[3::] # discount the folders and hidden files; change "3"

m = 123 # 123 was the number of mp3s in my file
prev = 130 # I have 130 pre-numbered mp3 files stashed away elsewhere...
oldname = [pairs[i][1] for i in range(0,m)]
newname = [str(i+prev)+' '+pairs[i][1] for i in range(0,m)]

os.chdir(D0)
print("Directory changed to "+D0) 
for i in range(0,m):
    os.rename(oldname[i],newname[i])
