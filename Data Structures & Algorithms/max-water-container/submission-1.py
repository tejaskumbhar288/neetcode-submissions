class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left, right = 0, len(heights)-1
        maxArea = 0

        while left < right:
            width = right - left
            breadth = min(heights[left], heights[right])
            area = width * breadth

            maxArea = max(maxArea, area)

            if heights[left] < heights[right]:
                left += 1

            else:
                right -= 1

        return maxArea
