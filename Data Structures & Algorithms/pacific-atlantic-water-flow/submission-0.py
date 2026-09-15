class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS = len(heights)
        COLS = len(heights[0])
        pacific = set()
        atlantic = set()
        directions = [
            (-1, 0), 
            (1, 0), 
            (0, -1), 
            (0, 1)
        ]

        def dfs(r, c, reachable):
            if (r, c) in reachable:
                return

            reachable.add((r, c))

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                #out of bound
                if nr < 0 or nr >= ROWS or nc < 0 or nc >= COLS:
                    continue

                #if adjacent are lower(we are taking reverse approach where we are checking
                # if which water block can reach pacific and atlantic)
                if heights[nr][nc] < heights[r][c]:
                    continue

                dfs(nr, nc, reachable)

        #pacific (top and left)
        for c in range(COLS):
            dfs(0, c, pacific)

        for r in range(ROWS):
            dfs(r, 0, pacific)

        #atlantic (bottom and right)
        for c in range(COLS):
            dfs(ROWS-1, c, atlantic)

        for r in range(ROWS):
            dfs(r, COLS-1, atlantic)

        result = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c ) in pacific and (r, c) in atlantic:
                    result.append([r, c])

        return result