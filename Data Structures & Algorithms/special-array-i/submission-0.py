class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        isParity = True
        isEven = True if nums[0]%2==0 else False
        
        for i in range(1, len(nums)):
            if nums[i] % 2 == 0:
                if isEven == True:
                    return False
                isEven = True

            elif nums[i] % 2 != 0:
                if isEven == False:
                    return False

                isEven = False
            

        return isParity
