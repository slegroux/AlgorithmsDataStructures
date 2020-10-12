"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""

import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""


phone_list = []

for line in texts:
    # T: O(N) (have to read through all list of size N)
    # S: O(N) (have to increase size of phone_list N times)
    phone_list.append(line[0])
    phone_list.append(line[1])

for line in calls:
    phone_list.append(line[0])
    phone_list.append(line[1])

# converting a list to a set of unique elements you have to go through all list elements T:O(N) and at most list i
# made of only unique elements so space neeeded for set would be S: O(N)
print("There are {} different telephone numbers in the records.".format(len(set(phone_list))))

# so overall 2*O(N) + O(N) = O(N) both time & space