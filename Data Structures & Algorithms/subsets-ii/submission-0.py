class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        ret = []

        sol = []

        nums.sort()

        def backtrack(i):

            if len(nums) == i:

                ret.append(sol[:])

                return

            sol.append(nums[i])
            
            backtrack(i+1)

            sol.pop()

            k = i+1

            while k < len(nums) and nums[i] == nums[k]:

                k += 1

            backtrack(k)


        backtrack(0)

        return ret


        