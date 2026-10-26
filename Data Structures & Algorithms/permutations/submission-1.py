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
                if used[i]:
                    continue

                #include
                path.append(nums[i])
                used[i] = True

                #Explore
                backtrack()

                #exclude
                path.pop()
                used[i] = False


        backtrack()
        return result