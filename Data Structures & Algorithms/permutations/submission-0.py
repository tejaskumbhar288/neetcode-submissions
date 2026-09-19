class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        used = [False] * len(nums)

        def backtrack():
            if len(nums) == len(path):
                result.append(path.copy())
                return

            for i in range(len(nums)):
                # Already used in current permutation
                if used[i]:
                    continue

                #choose
                path.append(nums[i])
                used[i] = True

                #explore
                backtrack()

                #undo
                path.pop()
                used[i] = False


        backtrack()
        return result