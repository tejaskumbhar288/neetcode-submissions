# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        res1 = []

        curr = head
        while curr:
            res1.append(curr.val)
            curr = curr.next

        left, right = 0, len(res1) - 1
        while left < right:
            if res1[left] != res1[right]:
                return False
            left += 1
            right -= 1

        return True
