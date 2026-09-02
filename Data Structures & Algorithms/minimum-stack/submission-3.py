class MinStack:

    def __init__(self):
        self.original_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.original_stack.append(val)

        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        temp = self.original_stack.pop()

        if self.min_stack and temp == self.min_stack[-1]:
            self.min_stack.pop()

    def top(self) -> int:
        if self.original_stack:
            return self.original_stack[-1]

    def getMin(self) -> int:
        if self.min_stack:
            return self.min_stack[-1]