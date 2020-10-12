"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

durations = {}

for line in calls:
    # T: O(n) go through list of size n
    # S: O(n) at most has to add n elements to dictionary
    if line[0] not in durations:
        durations[line[0]] = int(line[-1])
    else:
        durations[line[0]] += int(line[-1])
    
    if line[1] not in durations:
        durations[line[1]] = int(line[-1])
    else:
        durations[line[1]] += int(line[-1])

inverse_dict = {}
for v, k in durations.items():
    # T: O(n) go through all duratoins elements and create inverse_dict elements S: O(n)
    inverse_dict[k] = v

m = max(inverse_dict) # have to check all elements to see if larger than current max T: O(n) just create 1 new variable S: O(1)
phone = inverse_dict[m] # hash table to get value at key m: T: O(1)

# => overall complexity O(n) both S & T

print("{} spent the longest time, {} seconds, on the phone during September 2016.".format(phone, m))
