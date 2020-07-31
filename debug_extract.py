'''Script to filter the debug.log file. Generates per second log into sorted_debug.txt'''


import os.path
import linecache


# Counts the no. of lines in target file
def lines(fname):
    i = 0
    if os.path.exists(fname):
        with open(fname, 'r') as f:
            for i, l in enumerate(f):
                pass
        return i + 1

# Add elements to dictionary ONLY if not present
def add(dictionary, item):
    if item[0] not in dictionary.keys():
        dictionary[item[0]] = item[1]

# Convert ONLY numbers in string to a numeric value (ignores null strings)
def num(string):
    a = ''
    for i in string:
        if i.isalnum():
            a += i
    if a:
        return int(a)

d, f_o, f_i = {}, 'sorted_debug.txt', 'debug.log'

# Reading from debug.log
if os.path.exists(f_i):
    for i in range(1, lines(f_i) + 1, 13):
        add(d, [num(linecache.getline(f_i, i + 10)[11:13]), [i, num(linecache.getline(f_i, i)[11:13])]])

# Writing to sorted_debug.txt
with open(f_o, 'w') as f:
    for i in list(d.values()):
        for j in range(i[0], i[0] + 11):
            f.write(linecache.getline(f_i, j))
        f.write('\n\n')

print('Done parsing!')
