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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
from_bangalore = []

# T for time & S for space complexities

# T: O(n) because O(1) look for code in phone number in each of n line 
# S: O(n) n * O(1) for storing each code at each line 
for line in calls:
  if line[0][:5] == '(080)':
    code = []
    if line[1][:2] == '(0':
      i = 1
      while line[1][i] != ')':
        # S: O(1) need at most length of phone number-2 spaces for are code (if whole phone number was just the area code)
        code.append(line[1][i])
        i += 1
      from_bangalore.append(''.join(code))
    elif line[1][5] == ' ':
      if int(line[1][0]) == (7 or 8 or 9):
        from_bangalore.append(line[1][:4])
    elif line[1][:3] == '140':
      from_bangalore.append('140')

# T: O(n) (go through wole list to get set)
l = list(set(from_bangalore))
l.sort() # T: O(nlogn)

# overall complexity => T: O(nlogn) S: O(n)

print("The numbers called by people in Bangalore have codes:")
for i in l:
  print(i)


# Part B
count_outgoing = 0
count_ingoing = 0
for line in calls:
  if line[0][:5] == '(080)':
    count_outgoing += 1
    if line[1][:5] == '(080)':
      count_ingoing += 1


# # overal complexity:
# # T: O(n): go through at most list of N calls. each time check pattern for area code O(1). n*O(1) = O(n)
# # S: O(1) just update 2 var

p = round(count_ingoing / float(count_outgoing), 2)
print("{:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore.".format(p))
