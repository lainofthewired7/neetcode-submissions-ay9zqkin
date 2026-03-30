class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        ret = []

        sol = []

        def backtrack(leftCount, rightCount, length):

            if leftCount == n and rightCount == n:

                ret.append("".join(sol))

                return

            if leftCount > rightCount:

                sol.append(")")

                backtrack(leftCount, rightCount+1, length+1)

                sol.pop()

            if leftCount < n:

                sol.append("(")

                backtrack(leftCount+1, rightCount, length+1)

                sol.pop()
        
        backtrack(0, 0, 0)

        return ret

            

        

        
        