import os
import os.path
import re
import sys
import pdb

filename = 'locationTable'

if len(sys.argv) != 2:
    print "ERROR: need to input a location number"
    exit()

loc = sys.argv[1]
pos_loc = 0
neg_loc = 0
loc_list = [loc]

i = 0
for line in open(filename):
    i += 1
    splited_line = re.split(' |\t', line)
    if (3 != len(splited_line)):
        print "ERROR: data error in line:%d" % i
        exit()
    else:
        if loc == splited_line[0]:
            neg_loc = splited_line[1]
            pos_loc = splited_line[2]
            break

print pos_loc
print neg_loc

while (0 != int(neg_loc)):
    loc_list.insert(0, neg_loc)
    i = 0
    for line in open(filename):
        i += 1
        splited_line = re.split(' |\t', line)
        if (3 != len(splited_line)):
            print "ERROR: data error in line:%d" % i
            exit()
        else:
            if (int(neg_loc) == int(splited_line[0])):
                neg_loc = splited_line[1]
                break

while (0 != int(pos_loc)):
    loc_list.append(pos_loc)
    i = 0
    for line in open(filename):
        i += 1
        splited_line = re.split(' |\t', line)
        if (3 != len(splited_line)):
            print "ERROR: data error in line:%d" % i
            exit()
        else:
            if (int(pos_loc) == int(splited_line[0])):
                print line
                pos_loc = splited_line[2]
                break

outstr = ""

for __loc in loc_list:
    if (int(__loc) == int(loc)):
        outstr +=  "[%d] -> " % int(__loc)
    else:
        outstr +=  "%d -> " % int(__loc)

if (len(outstr) > 3):
    outstr = outstr[0:-3]

print outstr
