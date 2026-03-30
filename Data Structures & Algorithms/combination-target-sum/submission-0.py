class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        ret = []

        sol = []

        nums.sort()

        def backtrack(i, sum):

            if sum == target:

                ret.append(sol[:])

                return

            if sum > target or i == len(nums):

                return

            sol.append(nums[i])

            backtrack(i, sum+nums[i])

            sol.pop()

            backtrack(i+1, sum)
        
        backtrack(0, 0)

        return ret

            

                

        