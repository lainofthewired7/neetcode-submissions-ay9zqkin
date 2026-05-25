class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n  = len(nums)

        res = 0

        for i in range (n+1):

            res ^= i

        for i in range (n):

            res ^= nums[i]
        

        return res





            