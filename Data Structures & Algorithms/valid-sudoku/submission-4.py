class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        seen = set()

        for r in range(len(board)):
            for c in range(len(board[0])):
                d = board[r][c]

                if d == '.':
                    continue
                
                row_key = ("row_key", r, d)
                col_key = ("col_key", c, d)
                box_key = ("box_key", r//3, c//3, d)

                if row_key in seen or col_key in seen or box_key in seen:
                    return False

                seen.add(row_key)
                seen.add(col_key)
                seen.add(box_key)

        return True