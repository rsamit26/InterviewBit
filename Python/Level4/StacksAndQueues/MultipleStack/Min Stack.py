"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) – Push element x onto stack.
pop() – Removes the element on top of the stack.
top() – Get the top element.
getMin() – Retrieve the minimum element in the stack.
Note that all the operations have to be constant time operations.

Questions to ask the interviewer :

Q: What should getMin() do on empty stack?
A: In this case, return -1.

Q: What should pop do on empty stack?
A: In this case, nothing.

Q: What should top() do on empty stack?
A: In this case, return -1
"""


class Stack:
    def __init__(self):
        self.min = None
        self.stack = list()
    # function to get minimum element of the stack
    def getMin(self):
        if len(self.stack) == 0:
            return -1
        else:
            return self.min
    # function to return the top element
    def top(self):
        if len(self.stack) == 0:
            return -1
        top = self.stack[-1]
        if self.min > top:
            return self.min
        else:
            return top
    # function to pop the element from the stack
    def pop(self):
        if len(self.stack) == 0:
            return
        top = self.stack[-1]
        self.stack.pop()
        if top < self.min:
            self.min = 2*self.min-top
    # function to append element in the array
    def push(self, item):
        if len(self.stack) == 0:
            self.min = item
            self.stack.append(item)
            return
        if item < self.min:
            self.stack.append(2*item - self.min)
            self.min = item
        else:
            self.stack.append(item)

# Solution 2 : Using tupple as element

class Stack2:
    """Description::
    Operation       Stack                               Min     Top
    Push(10)        [(10,10)]                           10      (10,10)
    Push(9)         [(10,10), (9,9)]                    9       (9,9)
    getMin          [(10,10), (9,9)]                    9       (9,9)
    Push(8)         [(10,10), (9,9), (8,8)]             8       (8,8)
    getMin                  ""                          8       (8,8)
    Push(7)         [(10,10),(9,9),(8,8),(7,7)]         7       (7,7)
    getMin                  ""                          7       (7,7)
    Push(6)         [(10,10),(9,9),(8,8),(7,7),(6,6)]   6       (6,6)
    getMin                  ""                          6       (6,6)
    pop()           [(10,10),(9,9),(8,8),(7,7)]         7       (7,7)
    getMin                  ""                          7       (7,7)
    pop()           [(10,10), (9,9), (8,8)]             8       (8,8)



    """

    def __init__(self):
        self.stack = list()

    def push(self, item):
        if not self.stack:
            self.stack.append((item,item))  # appending element in form of tupple
        else:
            self.stack.append((item, min(item, self.stack[-1][1])))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        if self.stack:
            return self.stack[-1][0]
        else:
            return -1
    def getMin(self):
        if self.stack:
            return self.stack[-1][1]
        else:
            return -1


s = Stack2()
s.push(10)
s.push(9)
print(s.getMin())
s.push(8)
print(s.getMin())
s.push(7)
print(s.getMin())
s.push(6)
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
s.pop()
print(s.getMin())
