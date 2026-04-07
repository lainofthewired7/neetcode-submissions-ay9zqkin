class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ret = nums[0]

        minProduct = nums[0]

        maxProduct = nums[0]

        for i in range (1, len(nums)):

            curr = nums[i]

            maxProduct, minProduct = max(curr, curr*maxProduct, curr*minProduct), min(curr, curr*maxProduct, curr*minProduct)

            ret = max(ret, maxProduct)

        return ret









    

        