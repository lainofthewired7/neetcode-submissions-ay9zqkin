class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        maxLen = 1

        dp = [1] * n

        for i in range (n):

            for j in range (i-1, -1, -1):

                if nums[j] < nums[i]:

                    dp[i] = max(dp[i], dp[j] + 1)

        print(dp)

        return max(dp)




        