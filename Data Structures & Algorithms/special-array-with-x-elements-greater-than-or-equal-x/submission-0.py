class Solution:
    def specialArray(self, nums: List[int]) -> int:
        nums.sort()
        counter = 1

        for i in range(len(nums)-1, -1, -1):
            if nums[i] >= counter:
                if i > 0 and nums[i-1] < counter:
                    return counter
                if i == 0:
                    return counter

            counter += 1

        return -1