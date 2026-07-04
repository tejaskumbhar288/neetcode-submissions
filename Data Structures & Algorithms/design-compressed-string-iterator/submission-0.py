class StringIterator:

    def __init__(self, compressedString: str):
        self.s = compressedString
        self.ptr = 0
        self.ch = ''
        self.count = 0

    def next(self) -> str:
        if not self.hasNext():
            return ' '

        if self.count == 0:
            self.ch = self.s[self.ptr]
            self.ptr += 1

            num = 0
            while self.ptr < len(self.s) and self.s[self.ptr].isdigit():
                num = num * 10 + int(self.s[self.ptr])
                self.ptr +=  1

            self.count = num

        self.count -= 1
        return self.ch

    def hasNext(self) -> bool:
        return self.ptr < len(self.s) or self.count > 0


# Your StringIterator object will be instantiated and called as such:
# obj = StringIterator(compressedString)
# param_1 = obj.next()
# param_2 = obj.hasNext()
