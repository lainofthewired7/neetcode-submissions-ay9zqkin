class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        n = len(nums)

        dp = [[0 for _ in range (n)] for _ in range (2)]

        ret = []

        sol = []

        def backtrack(i):

            if i == n:

                if sum(sol) == target:

                    ret.append(sol[:])

                return

            sol.append(-nums[i])

            backtrack(i+1)

            sol.pop()

            sol.append(nums[i])

            backtrack(i+1)

            sol.pop()

        backtrack(0)

        return len(ret)



                








        

        