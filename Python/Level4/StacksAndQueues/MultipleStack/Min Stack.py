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

    def isEmpty(self):
        return len(self.stack) == 0

    def push(self, item):
        if self.isEmpty():
            self.min = item
            self.stack.append(0)
        else:
            self.stack.append(item - self.min)
            if item < self.min:
                self.min = item

    def pop(self):

        item = self.stack.pop()

        if item < 0:
            self.min = self.min - item

    def top(self):
        item = self.stack[-1]

        if item > 0:
            return item + self.min
        else:
            return self.min

    def getMin(self):
        return self.min
