class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        heights = heights + [0]
        maxArea = 0

        for i, h in enumerate(heights):
            while stack and heights[stack[-1]] >= h:
                height = heights[stack.pop()]
                
                #width
                if stack:
                    left = stack[-1]
                else:
                    left = -1

                width = i - left - 1
                maxArea = max(maxArea, height * width)

            stack.append(i)

        return maxArea
                