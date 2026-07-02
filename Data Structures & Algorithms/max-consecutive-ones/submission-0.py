class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        result = 0
        consecutive = 0

        for index, num in enumerate(nums):
            if num == 0:
                if result < consecutive:
                    result = consecutive
                consecutive = 0

            else:
                consecutive += 1
                if index == len(nums)-1:
                    if result < consecutive:
                        result = consecutive

        return result
