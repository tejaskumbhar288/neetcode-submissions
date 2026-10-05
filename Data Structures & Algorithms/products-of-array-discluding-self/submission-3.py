class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_prod = [1] * n
        suffix_prod = [1] * n
        result = [1] * n

        for i in range(1, n):
            prefix_prod[i] = prefix_prod[i-1] * nums[i-1]

        for j in range(n-2, -1, -1):
            suffix_prod[j] = suffix_prod[j+1] * nums[j+1]

        for i in range(n):
            result[i] = prefix_prod[i] * suffix_prod[i]

        return result