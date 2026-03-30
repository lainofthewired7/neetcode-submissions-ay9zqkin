class Solution:
    def solve(self, board: List[List[str]]) -> None:

        def dfs(row, col):

            if min(row, col) < 0 or row == len(board) or col == len(board[0]):
                
                return

            if board[row][col] != "O":

                return

            if board[row][col] == "#":

                return

            board[row][col] = "#"

            dfs(row+1, col)

            dfs(row-1, col)

            dfs(row, col+1)

            dfs(row, col-1)

        for i in range (len(board)):

            dfs(i, 0)

            dfs(i, len(board[0])-1)

        for j in range (len(board[0])):

            dfs(0, j)

            dfs(len(board)-1, j)
                


        for i in range (len(board)):

            for j in range (len(board[0])):

                if board[i][j] == "O":

                    board[i][j] = "X"

                if board[i][j] == "#":

                    board[i][j] = "O"


        


        