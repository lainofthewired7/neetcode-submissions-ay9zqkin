class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        q = deque()

        seen = set()

        for i in range (len(grid)):

            for j in range (len(grid[0])):

                if grid[i][j] == 2:

                    q.append((i, j))

        def inbounds(i, j):

            if min(i, j) < 0 or i == len(grid) or j == len(grid[0]):

                return False

            return True

        time = -1

        while q:

            time += 1

            for _ in range (len(q)):

                curr = q.popleft()

                grid[curr[0]][curr[1]] = 2

                if inbounds(curr[0]+1, curr[1]) and grid[curr[0]+1][curr[1]] == 1:
                    q.append((curr[0]+1, curr[1]))

                if inbounds(curr[0]-1, curr[1]) and grid[curr[0]-1][curr[1]] == 1:
                    q.append((curr[0]-1, curr[1]))
                
                if inbounds(curr[0], curr[1]+1) and grid[curr[0]][curr[1]+1] == 1:
                    q.append((curr[0], curr[1]+1))
                
                if inbounds(curr[0], curr[1]-1) and grid[curr[0]][curr[1]-1] == 1:
                    q.append((curr[0], curr[1]-1))

            

        for i in range (len(grid)):

            for j in range (len(grid[0])):

                if grid[i][j] == 1:

                    return -1

        return time if time != -1 else 0



            

        


        



        
        