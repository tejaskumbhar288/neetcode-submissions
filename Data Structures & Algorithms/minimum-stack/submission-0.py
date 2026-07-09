class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        #pushing in minStack
        if len(self.minStack) > 0:
            top = self.minStack[-1]
            if top > val:
                self.minStack.append(val)
            else:
                self.minStack.append(top)

        else:
            self.minStack.append(val)

    def pop(self) -> None:
        #pop from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return -1

    def getMin(self) -> int:
        if len(self.minStack) > 0:
            return self.minStack[-1]
        else:
            return -1
        
