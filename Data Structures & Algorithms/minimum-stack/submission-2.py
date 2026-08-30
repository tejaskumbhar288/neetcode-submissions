class MinStack:

    def __init__(self):
        self.stack = [] #main stack
        self.min_stack = [] #stored min at each point

    def push(self, val: int) -> None:
        self.stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)


    def pop(self) -> None:
        if self.stack:
            temp = self.stack[-1]

            if self.min_stack and temp == self.min_stack[-1]:
                self.min_stack.pop()
                
            self.stack.pop()


    def top(self) -> int:
        if self.stack:
            return self.stack[-1]

        

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]

        
