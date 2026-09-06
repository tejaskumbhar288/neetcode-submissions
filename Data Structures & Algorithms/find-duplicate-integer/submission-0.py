class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #floyd cycle detection problem
        # Phase 1: Find intersection point inside the cycle

        slow = nums[0]
        fast = nums[0]

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break

        # Phase 2: Find the entrance of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow