import os
import os.path
import datetime
import re
import pdb

# rootdir = "/home/guanzx/python_src"
rootdir = "."
suffix  = ".py"
Const_File_Format = [".txt"]
additional_hour = 10

events_count = 0
max_event_count = 65535

os.system('rm -rf Out')
os.mkdir("Out")

for parent,dirnames,filenames in os.walk(rootdir):
    # for dirname in  dirnames:
    #     print "parent is:" + parent
    #     print  "dirname is" + dirname

    for filename in filenames:
        if os.path.splitext(filename)[1] in Const_File_Format:
            file_object = open("./Out/" + filename + "_out", 'w')
            print filename + " ..."
            splited_file_time = re.split('_', filename)
            if (5 == len(splited_file_time)):
                # print "filename is:" + filename
                file_date_str = "2016" + splited_file_time[2] + splited_file_time[3]
                file_date = datetime.datetime.strptime(file_date_str, "%Y%m%d%H%M%S")

                for line in open(filename):
                    if line.find('Evt=') > 0:
                        splited_rec = re.split('\.|\:|\[|\]', line)
                        if (6 == len(splited_rec)):
                            time_offset = datetime.timedelta(hours = (int(splited_rec[1]) + additional_hour), minutes = int(splited_rec[2]), seconds = int(splited_rec[3]), milliseconds = int(splited_rec[4]))
                            actul_time = file_date + time_offset
                            actul_time_str = actul_time.strftime("%Y-%m-%d %H:%M:%S.%f")[:-3]
                            # print actul_time_str
                            # print line
                            splited_line = re.split('\[|\]', line)
                            if (3 == len(splited_line)):
                                newline = splited_line[0] + "[" + actul_time_str + "]" + splited_line[-1]
                                file_object.writelines(newline)
                                events_count += 1

            file_object.close()
print "%d event(s) output ..." % events_count

os.system('cd Out && cat *out | grep "Evt=" > all_events')
os.system('cd Out && rm *out')

locs = [0] * max_event_count
for line in open("./Out/all_events"):
    match = re.split('=|\,', line)
    locs[int(match[3])] = 1

loclist_file_object = open("./Out/loc_list", 'w')
for i in range(0, len(locs)):
    # location exist
    if (1 == int(locs[i])):
        loclist_file_object.writelines("Loc:%d\n" % i)
        for line in open("./Out/all_events"):
            match = re.split('=|\,', line)
            if (int(match[3]) == i):
                line = line.strip('\r\n')
                loclist_file_object.writelines("%s\n" % line)
        loclist_file_object.writelines("\n")
loclist_file_object.close()

print 'done'
