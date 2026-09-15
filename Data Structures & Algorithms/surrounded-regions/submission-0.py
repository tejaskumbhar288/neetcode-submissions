class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # 1. Find O's on the boundary
        # 2. DFS/BFS from those O's
        # 3. Mark every reachable O as SAFE
        # 4. Scan the board
        # 5. O  → X
        # 6. SAFE → O
        ROWS = len(board)
        COLS = len(board[0])
        directions = [
            (-1, 0), 
            (1, 0), 
            (0, -1), 
            (0, 1)
        ]

        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return

            if board[r][c] != 'O':
                return

            board[r][c] = 'T'

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                dfs(nr, nc)

            
        #top row
        for c in range(COLS):
            if board[0][c] == 'O':
                dfs(0, c)

        #left column
        for r in range(ROWS):
            if board[r][0] == 'O':
                dfs(r, 0)

        #bottom row
        for c in range(COLS):
            if board[ROWS-1][c] == 'O':
                dfs(ROWS-1, c)

        #right column
        for r in range(ROWS):
            if board[r][COLS-1] == 'O':
                dfs(r, COLS - 1)

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == 'T':
                    board[r][c] = 'O'
                else:
                    board[r][c] = 'X'
