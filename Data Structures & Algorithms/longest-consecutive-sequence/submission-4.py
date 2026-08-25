class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        #The approach is we just have to check if (n - 1) is in set or not. if yes then we are in middle of someones chain. if not then start a new chain
        num_set = set(nums)
        longest = 0

        for num in nums:
            if (num - 1) not in num_set:
                #This is one chain
                length = 1
                while (num + length) in num_set:
                    length += 1

                longest = max(longest, length)

        return longest