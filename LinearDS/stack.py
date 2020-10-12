#!/usr/bin/env python

# implementing stack with linkedlist
class Node():
    def __init__(self, value=None):
        self.value = value
        self.next = next

# push/pop new node to head
class Stack():
    def __init__(self, value):
        self.head = Node(value)
    
    def push(self, value):
        current = self.head
        new = Node(value)
        if current == None:
            self.head = new
        
        else:
            new.next = self.head
            self.head = new
    
    def pop(self):
        current = self.head
        if current == None:
            return
        self.head = current.next
        return(current.value)


# stack with python lists
class Stack2():
    def __init__(self):
        self.stack = []
    
    def size(self):
        return(len(self.stack))
    
    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() == 0:
            return(None)
        else:
            return(self.stack.pop())


if __name__ == "__main__":
    # s = Stack(0)
    # s.push(1)
    # s.push(2)
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    # print(s.pop())
    s = Stack2()
    s.push(1)
    s.push(2)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())

    