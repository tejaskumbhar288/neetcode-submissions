class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sum = nums[0]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                maxSum = max(maxSum, sum)
                print("MaxSum = ", maxSum)
                sum = 0

            sum += nums[i]
            print("Sum = ", sum)

        maxSum = max(maxSum, sum)
        return maxSum

            
