class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = {i:set() for i in range (9)}

        cols = {i:set() for i in range (9)}

        squares = {i:set() for i in range (9)}

        for i in range (len(board)):

            for j in range (len(board[0])):

                val = board[i][j]

                square = (i // 3) * 3 + (j // 3)

                if val == ".":

                    continue

                if val in rows[i] or val in cols[j] or val in squares[square]:

                    return False

                rows[i].add(val)

                cols[j].add(val)

                squares[square].add(val)

        return True





        