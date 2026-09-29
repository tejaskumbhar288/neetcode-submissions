from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        rows = len(grid)
        cols = len(grid[0])
        INF = 2147483647
        directions = [
            (-1, 0),
            (1, 0), 
            (0, -1),
            (0, 1)
        ]

        #First fill all the treasure islands in queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        while queue:
            (r, c) = queue.popleft()

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc

                if new_r < 0 or new_r >= rows:
                    continue

                if new_c < 0 or new_c >= cols:
                    continue

                if grid[new_r][new_c] != INF:
                    continue

                grid[new_r][new_c] = grid[r][c] + 1

                queue.append((new_r, new_c))