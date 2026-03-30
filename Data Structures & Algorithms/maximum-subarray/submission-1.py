class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        if not nums:

            return 0

        maxSum, summ = nums[0], 0

        for i in range (len(nums)):

            summ += nums[i]

            maxSum = max(maxSum, summ)

            if summ < 0:

                summ = 0

        return maxSum


        