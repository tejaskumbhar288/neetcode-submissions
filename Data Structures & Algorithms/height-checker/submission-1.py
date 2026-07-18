class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        expected = sorted(heights)
        total = 0

        for i in range(len(heights)):
            if expected[i] != heights[i]:
                total += 1

            
        return total