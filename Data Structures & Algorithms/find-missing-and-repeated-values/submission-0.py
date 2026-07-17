class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0] *2
        my_dict = {}
        num = 0
        n = len(grid) * len(grid)
        print("n = ", n)
        actual_sum = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] in my_dict:
                    num = grid[i][j]

                my_dict[grid[i][j]] = 1
                actual_sum += grid[i][j]

        
        print("Actual sum = ", actual_sum)
        total = (n * (n + 1))//2
        print("total = ", total)
        temp = actual_sum - num
        print("temp = ", temp)
        missing = total - temp
        print("missing = ", missing)
        return [num, missing]
