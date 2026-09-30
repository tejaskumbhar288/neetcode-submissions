class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(len(nums) - 1):
            # How far can we reach from this index?
            farthest = max(farthest, i + nums[i])

            # We have reached the end of our current jump range
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps