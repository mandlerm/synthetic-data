"""
temporary solution for taking a dataset and syphening off some rows for current use and the remaining rows in a 'pool' file for future use.

"""
import csv
import sys 
import math

NUM_ROWS_NEEDED = 47935

# input file
filename = sys.argv[1]
f = open(filename,"r+")
r = csv.reader(f)

# test and train output files
f = filename.split('.')[0]

print(f)
current_file = open(f"current_{f}.csv", "a+")
current_writer = csv.writer(current_file)

pool_file = open(f"pool{f}.csv", "a+")
pool_writer = csv.writer(pool_file)

###################################
# Currently hard coded based on how many
# rows are needed from the file
##################################
row_count = math.floor(len(list(r)))

increment = math.floor(row_count / NUM_ROWS_NEEDED)
count = 0
current_count = 0
pool_count = 0
print(increment)

with open(filename) as f:
            csvreader = csv.reader(f)
            headers = next(csvreader)
            current_writer.writerow(headers)
            pool_writer.writerow(headers)

            for row in csvreader:
                count += 1
                if ((count % increment) == 0):
                    current_count += 1
                    current_writer.writerow(row)
                else:
                    pool_count += 1
                    pool_writer.writerow(row)
                    


print(f"{row_count}: pool: {pool_count} current {current_count}")