"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #handle empty list
        if not head:
            return None

        #step 1: create a mapping from original to copy 
        old_to_copy = {}

        curr = head
        while curr:
            #create a copy of this node (just the value for now)
            old_to_copy[curr] = Node(curr.val)
            curr = curr.next

        #step 2: connect next and random pointers
        curr = head
        while curr:
            #Get the copy of the current node
            copy = old_to_copy[curr]

            #set its next pointer to the copy of curr.next
            copy.next = old_to_copy.get(curr.next)

            #set its random pointer to the copy of curr.random
            copy.random = old_to_copy.get(curr.random)

            curr = curr.next

        #return the copy of the head
        return old_to_copy[head]

        

        

        