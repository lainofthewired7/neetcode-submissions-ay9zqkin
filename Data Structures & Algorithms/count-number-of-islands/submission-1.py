class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        seen = set()

        islands = 0

        def dfs(x, y):

            if min(x, y) < 0 or x >= len(grid) or y >= len(grid[0]):

                return
            
            if (x, y) in seen:

                return

            if grid[x][y] == "0":

                return

            seen.add((x,y))

            dfs(x+1, y)

            dfs(x-1, y)

            dfs(x, y+1)

            dfs(x, y-1)
        

        ROW = len(grid)
        COL = len(grid[0])

        for i in range (ROW):
            for j in range (COL):
                if (i, j) in seen:
                    continue
                if grid[i][j] == "1":
                    dfs(i, j)
                    islands +=1

        

        

        return islands