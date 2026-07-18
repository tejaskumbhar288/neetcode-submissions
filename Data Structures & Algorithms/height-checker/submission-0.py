class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        temp = heights.copy()
        temp.sort()
        total = 0

        for i in range(len(heights)):
            if temp[i] != heights[i]:
                total += 1

            
        return total