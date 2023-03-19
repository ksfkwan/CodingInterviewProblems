'''
Polymorphism is a key concept in OOP.
'''

class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val):
        self.stack.append(val)
        self.minStack.append(min(val, self.minStack[-1] if self.minStack else val))

    def pop(self):
        self.stack.pop(-1)
        self.minStack.pop(-1)

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
print(obj.getMin())
obj.pop()
print(obj.top())
print(obj.getMin())
