#!/usr/bin/env python

class Queue:
    def __init__(self):
        self.q = []

    def size(self):
        return(len(self.q))
    
    def enqueue(self,value):
        self.q.append(value)

    def dequeue(self):
        if q.size() == 0:
            return(None)
        return(self.q.pop(0))


q = Queue()
q.enqueue('a')
q.enqueue('b')
q.enqueue('c')

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())