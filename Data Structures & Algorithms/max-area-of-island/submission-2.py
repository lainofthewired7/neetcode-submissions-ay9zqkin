class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        if not grid:

            return 0

        maxArea = 0

        area = 0

        def dfs(row, col):

            if min(row, col) < 0 or row == len(grid) or col == len(grid[0]):

                return 0

            if grid[row][col] == 0:

                return 0

            grid[row][col] = 0

            return 1 + dfs(row+1, col) + dfs(row-1, col) + dfs(row, col+1) + dfs(row, col-1)
            


        for i in range (len(grid)):

            for j in range (len(grid[0])):

                area = dfs(i, j)

                maxArea = max(area, maxArea)

        return maxArea

                


        