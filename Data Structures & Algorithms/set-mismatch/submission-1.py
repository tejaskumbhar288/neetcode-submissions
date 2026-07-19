class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        my_set = set()
        duplicate = -1
        missing = -1
        total = 0
        expected_sum = 0
        n = len(nums)

        for num in nums:
            if num in my_set:
                duplicate = num

            my_set.add(num)
            total += num

        expected_sum = (n * (n + 1))//2
        missing = expected_sum - (total - duplicate)

        return [duplicate, missing]

        
