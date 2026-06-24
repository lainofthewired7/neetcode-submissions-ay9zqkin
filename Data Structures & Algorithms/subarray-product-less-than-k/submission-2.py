class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        l = 0

        count = 0

        currProd = 1

        if len(nums) == 1 and nums[0] < k:

            return 1

        if k <= 1:

            return 0

        for r in range(len(nums)):

            currProd *= nums[r]

            while currProd >= k:

                currProd //= nums[l]

                l+=1

            

            count += (r-l+1)

        return count










        