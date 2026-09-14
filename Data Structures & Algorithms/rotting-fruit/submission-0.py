from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        total_fresh = 0
        total_time = 0
        directions = [
            (-1, 0), 
            (1, 0), 
            (0, -1), 
            (0, 1)
        ]
        queue = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    total_fresh += 1

                elif grid[r][c] == 2:
                    queue.append((r, c))

        while queue and total_fresh > 0:
            total_time += 1
            for _ in range(len(queue)):
                r, c = queue.popleft()

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if new_r < 0 or new_r >= rows:
                        continue

                    if new_c < 0 or new_c >= cols:
                        continue

                    if grid[new_r][new_c] != 1:
                        continue

                    grid[new_r][new_c] = 2
                    total_fresh -= 1
                    queue.append((new_r, new_c))

        if total_fresh == 0:
            return total_time

        else:
            return -1