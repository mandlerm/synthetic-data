import csv
import sys 
import math

# input file
filename = sys.argv[1]
f = open(filename,"r+")
r = csv.reader(f)

# test and train output files
f = filename.split('.')[0]

test_file = open(f"{f}-test.csv", "a+")
test_writer = csv.writer(test_file)

train_file = open(f"{f}-train.csv", "a+")
train_writer = csv.writer(train_file)

###################################
# Currently hard coded at 10%. Calculate 
# for the number of rows that should be
# in the test set.
# Then calculate the skip number to achieve
# that many rows. Parse the file into 
# test and train csv's at the 90/10 split
##################################
row_count = math.floor(len(list(r)))
test_count = row_count * .1
increment = math.floor(row_count / test_count)

count = 0
test_count = 0
train_count = 0
print(increment)

with open(filename) as f:
            csvreader = csv.reader(f)
            headers = next(csvreader)
            test_writer.writerow(headers)
            train_writer.writerow(headers)

            for row in csvreader:
                count += 1
                if ((count % increment) == 0):
                    test_count += 1
                    test_writer.writerow(row)
                else:
                    train_count += 1
                    train_writer.writerow(row)


print(f"total: {row_count}: test: {test_count} train {train_count}")