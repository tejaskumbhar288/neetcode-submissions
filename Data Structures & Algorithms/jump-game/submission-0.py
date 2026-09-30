class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0

        for i in range(len(nums)):

            # If we can't even reach i,
            # we definitely can't continue.
            if i > farthest:
                return False

            # Extend our maximum reachable position.
            farthest = max(farthest, i + nums[i])

        return True
