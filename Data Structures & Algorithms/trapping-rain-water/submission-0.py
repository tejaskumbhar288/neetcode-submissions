class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) -1

        maxLeft = 0
        maxRight = 0
        water = 0

        for i in range(len(height)):
            maxLeft = max(maxLeft, height[left])
            maxRight = max(maxRight, height[right])

            if maxLeft <= maxRight:
                left += 1
                water += maxLeft - height[i]
            else:
                right -= 1
                water += maxRight - height[i]
            
        return water
