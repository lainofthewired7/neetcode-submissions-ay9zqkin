class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        q = deque()

        seen = set()

        for i in range (len(grid)):
            for j in range (len(grid[0])):

                if grid[i][j] == 0:

                    q.append((i, j))

        depth = 0

        while q:

            for _ in range (len(q)):

                curr = q.popleft()

                if curr in seen:

                    continue

                if min(curr[0], curr[1]) < 0 or curr[0] == len(grid) or curr[1] == len(grid[0]):

                    continue

                if grid[curr[0]][curr[1]] == -1:

                    continue

                grid[curr[0]][curr[1]] = depth

                seen.add(curr)

                q.append((curr[0]+1, curr[1]))

                q.append((curr[0]-1, curr[1]))

                q.append((curr[0], curr[1]+1))

                q.append((curr[0], curr[1]-1))

            depth += 1



        

        
        