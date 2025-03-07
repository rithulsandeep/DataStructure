class MinMaxStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.max_stack = []

    def push(self, x):
        self.stack.append(x)
        if not self.min_stack or x <= self.min_stack[-1]:
            self.min_stack.append(x)
        if not self.max_stack or x >= self.max_stack[-1]:
            self.max_stack.append(x)

    def pop(self):
        if not self.stack:
            return None
        popped = self.stack.pop()
        if popped == self.min_stack[-1]:
            self.min_stack.pop()
        if popped == self.max_stack[-1]:
            self.max_stack.pop()
        return popped

    def top(self):
        return self.stack[-1] if self.stack else None

    def getMin(self):
        return self.min_stack[-1] if self.min_stack else None

    def getMax(self):
        return self.max_stack[-1] if self.max_stack else None

# Example Usage
    
stack = MinMaxStack()
stack.push(3)
stack.push(5)
stack.push(2)
print(stack.getMin())  # 2
print(stack.getMax())  # 5
stack.pop()
print(stack.getMin())  # 3
