class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #Monotonic solution
        stack = []
        nextGreater = {}

        for i in range(len(nums2)):
            curr = nums2[i]

            if len(stack) == 0:
                stack.append(curr)

            else:
                while len(stack)!=0 and curr > stack[-1]:
                    num = stack[-1]
                    stack.pop()
                    nextGreater[num] = curr
                
                stack.append(curr)

        while len(stack) != 0:
            num = stack[-1]
            stack.pop()
            nextGreater[num] = -1

        result = []

        for num in nums1:
            result.append(nextGreater[num])

        return result
        