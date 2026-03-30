class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        ret = []

        sol = []

        def backtrack(i):

            if i == len(nums):

                ret.append(sol[:])
                return

            #dont pick this number
            backtrack(i+1)

            #pick this number

            sol.append(nums[i])
            backtrack(i+1)
            sol.pop() #pops number that was just appended


        backtrack(0)

        return ret

        