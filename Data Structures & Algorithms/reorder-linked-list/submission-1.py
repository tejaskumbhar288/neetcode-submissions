# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #step 1 : find the middle
        #step 2: reverse the second half
        #Step 3: merge both list one by one
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        second = slow.next
        slow.next = None #this is where first half ends

        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt

        second = prev

        first = head
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2



