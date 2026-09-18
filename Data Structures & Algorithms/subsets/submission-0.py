class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []

        def backtrack(i):
            if i == len(nums):
                result.append(path.copy())
                return

            #choice 1: take nums[i]
            path.append(nums[i])
            backtrack(i + 1)
            path.pop()

            #choice 2: dont take
            backtrack(i + 1)

        backtrack(0)
        return result

