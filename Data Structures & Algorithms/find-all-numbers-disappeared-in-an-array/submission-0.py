class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = []

        for i in range(len(nums)):
            num = nums[i]
            index = abs(num) - 1
            print("Index = ", index)
            print("Nums[index] = ", nums[index])
            if nums[index] > 0:
                nums[index] = nums[index] * (-1)
            
            print("After if nums[index] = ", nums[index])

            
        print(nums)
        for i in range(len(nums)):
            if nums[i] > 0:
                result.append(i + 1)

        return result