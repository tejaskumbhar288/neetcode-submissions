class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Deque:
    
    def __init__(self):
        self.head = ListNode(-1)
        self.tail = ListNode(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def isEmpty(self) -> bool:
        return self.head.next == self.tail

    def append(self, value: int) -> None:
        newNode = ListNode(value)
        #You have to insert newNode between last and tail

        last = self.tail.prev  # this is last node
        last.next = newNode
        newNode.prev = last
        newNode.next = self.tail
        self.tail.prev = newNode

    def appendleft(self, value: int) -> None:
        newNode = ListNode(value)
        #You have to append newNode between head and first

        first = self.head.next #This is first element
        self.head.next = newNode
        newNode.prev = self.head

        newNode.next = first
        first.prev = newNode

    def pop(self) -> int:
        if self.isEmpty():
            return -1

        last = self.tail.prev
        value = last.val
        prev_node = last.prev
        prev_node.next = self.tail
        self.tail.prev = prev_node
        return value

    def popleft(self) -> int:
        if self.isEmpty():
            return -1

        first = self.head.next
        value = first.val
        next_node = first.next
        next_node.prev = self.head
        self.head.next = next_node

        return value

