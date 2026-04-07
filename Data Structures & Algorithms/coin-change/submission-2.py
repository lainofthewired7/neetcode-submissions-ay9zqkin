class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        if amount == 0:

            return 0

        n = amount

        dp = [float('inf')] * (n+1)

        dp[0] = 0

        for i in range (1, n+1):

            for coin in coins:

                prev = i - coin

                if prev >= 0:

                    dp[i] = min(dp[prev]+1, dp[i])
        
        if dp[amount] == float('inf'):

            return -1

        else:

            return dp[amount]



                



            

        

        

        

            

        

        
        