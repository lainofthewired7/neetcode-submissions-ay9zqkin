class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        atlantic = set()

        pacific = set()

        def dfs(row, col, dfsSet, prevHeight):

            if min(row, col) < 0 or row == len(heights) or col == len(heights[0]):

                return

            if heights[row][col] < prevHeight:

                return

            if (row, col) in dfsSet:

                return

            dfsSet.add((row, col))

            dfs(row+1, col, dfsSet, heights[row][col])

            dfs(row-1, col, dfsSet, heights[row][col])

            dfs(row, col+1, dfsSet, heights[row][col])

            dfs(row, col-1, dfsSet, heights[row][col])


        for row in range (len(heights)):

            dfs(row, 0, pacific, -1)

            dfs(row, len(heights[0])-1, atlantic, -1)
                

        for col in range (len(heights[0])):

            dfs(0, col, pacific, -1)

            dfs(len(heights)-1, col, atlantic, -1)

        return list(atlantic & pacific)

        
        
        