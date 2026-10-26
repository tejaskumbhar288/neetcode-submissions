class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []

        def backtrack(start, path):
            # Every current subset is a valid answer
            result.append(path.copy())

            for i in range(start, len(nums)):
                # Skip duplicates at the same recursion level
                if i > start and nums[i] == nums[i-1]:
                    continue

                #choose
                path.append(nums[i])

                #explore
                backtrack(i+1, path)

                #undo
                path.pop()


        backtrack(0, [])
        return result