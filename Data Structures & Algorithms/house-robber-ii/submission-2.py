class Solution:
    def rob(self, nums: List[int]) -> int:
        #helper linear solution of House Robber I
        def robber_linear(nums):
            prev2 = 0
            prev1 = 0

            for money in nums:
                temp = max(prev1, prev2 + money)

                prev2 = prev1
                prev1 = temp

            return prev1

        if len(nums) == 1:
            return nums[0]

        return max(robber_linear(nums[:-1]), robber_linear(nums[1:]))