from os import walk
import os
# os.path.getsize('C:\\Python27\\Lib\\genericpath.py')

mypath = '../SecLists/Passwords/'
f = []
for (dirpath, dirnames, filenames) in walk(mypath):
    f.extend(filenames)
    break

# get only txt files
for i in reversed(range(len(f))):
    if 'txt' not in f[i]:
        f.pop(i)
# order from smallest to largest
for i in range(len(f)):
    for j in range(len(f) - 1 - i):
        if os.path.getsize(mypath + f[j]) > os.path.getsize(mypath + f[j + 1]):
            t = f[j]
            f[j] = f[j + 1]
            f[j + 1] = t

words = set()

for i in range(len(f)):
    file1 = open(mypath + f[i], 'r')
    Lines = file1.readlines()
    for l in Lines:
        words.add(l.strip())
# print(words)
with open('wordlist.txt', 'w') as filehandle:
    filehandle.writelines("%s\n" % word for word in words)
