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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

outgoing_call = set()
ingoing_call = set()
outgoing_text = set()
ingoing_text = set()

for line in calls:
    outgoing_call.add(line[0])
    ingoing_call.add(line[1])

for line in texts:
    outgoing_text.add(line[0])
    ingoing_text.add(line[1])

# T: union O(n)
# S: O(n)
telemarket = list(outgoing_call - ingoing_call - outgoing_text - ingoing_text)
# T: O(nlog(n))
telemarket.sort()

print("These numbers could be telemarketers: ")
[ print(i) for i in telemarket ]

# => overall complexity: T: O(nlog(n)) S: O(n)