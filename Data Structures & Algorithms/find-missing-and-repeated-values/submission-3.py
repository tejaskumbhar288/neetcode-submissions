class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0] *2
        seen = set()
        num = 0
        n = len(grid)
        total_elements = n * n
        actual_sum = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in seen:
                    num = grid[i][j]

                seen.add(grid[i][j])
                actual_sum += grid[i][j]

        
        total = (total_elements * (total_elements + 1))//2
        temp = actual_sum - num
        missing = total - temp
        return [num, missing]
