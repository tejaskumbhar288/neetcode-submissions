class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        my_set = set()
        duplicate = -1
        missing = -1
        total = 0
        actual_sum = 0
        n = len(nums)

        for num in nums:
            if num in my_set:
                duplicate = num

            my_set.add(num)
            total += num

        actual_sum = (n * (n + 1))//2
        total = total - duplicate
        missing = actual_sum - total

        return [duplicate, missing]

        
