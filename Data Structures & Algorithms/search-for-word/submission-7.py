class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def backtrack(letterIndex, coords, seen):

            if coords[0] < 0 or coords[0] == len(board):
                
                return

            if coords[1] < 0 or coords[1] == len(board[coords[0]]):
                
                return

            if word[letterIndex] != board[coords[0]][coords[1]]:

                return

            if letterIndex == len(word)-1:

                return True
                
            if (coords[0]+1, coords[1]) not in seen:

                newCoords = (coords[0]+1, coords[1])

                seen.add(newCoords)

                if backtrack(letterIndex+1, newCoords, seen):
                    return True

                if newCoords in seen:
                    seen.remove(newCoords)

            if (coords[0]-1, coords[1]) not in seen:

                newCoords = (coords[0]-1, coords[1])

                seen.add(newCoords)

                if backtrack(letterIndex+1, newCoords, seen):
                    return True

                if newCoords in seen:
                    seen.remove(newCoords)

            if (coords[0], coords[1]+1) not in seen:

                newCoords = (coords[0], coords[1]+1)

                seen.add(newCoords)

                if backtrack(letterIndex+1, newCoords, seen):
                    return True

                if newCoords in seen:
                    seen.remove(newCoords)
                
            if (coords[0], coords[1]-1) not in seen:

                newCoords = (coords[0], coords[1]-1)

                seen.add(newCoords)

                if backtrack(letterIndex+1, newCoords, seen):
                    return True

                if newCoords in seen:
                    seen.remove(newCoords)

            return False

        found = False

        for i in range (len(board)):
            for j in range(len(board[i])):

                if board[i][j] == word[0]:

                    found = found or backtrack(0, (i, j), {(i,j)})

        return found
            
        