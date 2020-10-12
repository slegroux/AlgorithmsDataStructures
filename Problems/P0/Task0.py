"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    # time complexity (T) : O(n) (n = number of lines in text document)
    # space complexity (S): O(n) (list of n lines of fixed length)
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
# T: O(1) accessing an element in python list isin constant time (!= linked list)
# S: O(1) constant memory
print("First record of texts, {} texts {} at time {}".format(texts[0][0], texts[0][1], texts[0][2]))
last = calls[-1]
print("Last record of calls, {} calls {} at time {}, lasting {} seconds".format(last[0], last[1], last[2], last[3]))