class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()

        ret = []

        sol = []

        def backtrack(i, sum):

            if sum == target:

                ret.append(tuple(sol[:]))

            if sum > target or i == len(candidates):

                return

            sol.append(candidates[i])

            backtrack(i+1, sum+candidates[i])

            sol.pop()

            backtrack(i+1, sum)

        backtrack(0, 0)

        ret = set(ret)

        ret = list(ret)

        ret = [list(i) for i in ret]

        return ret

            




        