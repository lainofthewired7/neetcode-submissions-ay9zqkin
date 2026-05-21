class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        memo = {}

        def backtrack (i, curSum):

            if (i, curSum) in memo:

                return memo[(i, curSum)]

            if i == len(nums):

                return curSum == target

            memo[(i, curSum)] = (backtrack(i+1, curSum + nums[i]) + 
            backtrack(i+1, curSum-nums[i]))

            return memo[((i, curSum))]

        return backtrack(0, 0)

            


        