import csv 
import sys 

# Arg 1 = name for output file
# Arg 2+ are input files to contatenate into single output file

out_file = sys.argv[1]

num_files = len(sys.argv) 

f = open(out_file, 'a+')
fw = csv.writer(f)
print("**************")
print(out_file)
print(num_files)
# fw.writerow(['row', 'text', 'hate-speech'])
print("/n*************/n")
count = 0
x = range(2, num_files)
for n in x:   
    count = 0
    cf = open(sys.argv[n], 'r')
    csv_reader = csv.reader(cf)
    next(csv_reader)
    for row in csv_reader:
        fw.writerow(row)
        count += 1
    print(sys.argv[n], ": ", count)
print("count is ", count)
f.close()
