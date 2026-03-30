class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        ret = []

        sol = []

        def backtrack(i, sum):

            if sum == target:

                if sol in ret:

                    return

                ret.append(sol[:])

                return

            if len(candidates) == i or sum > target:

                return

            sol.append(candidates[i])

            backtrack(i+1, sum+candidates[i])

            sol.pop()

            backtrack(i+1, sum)

        backtrack(0, 0)

        return ret
            

            

            

            


        