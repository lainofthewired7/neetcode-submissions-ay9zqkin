class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        ret = nums[0]

        minProduct = nums[0]

        maxProduct = nums[0]

        for i in range (1, len(nums)):

            curr = nums[i]

            prevMax = maxProduct

            prevMin = minProduct

            maxProduct = max(curr, curr*prevMax, curr*prevMin)

 
            minProduct = min(curr, curr*prevMax, curr*prevMin)
            

            ret = max(ret, maxProduct)

        return ret









    

        