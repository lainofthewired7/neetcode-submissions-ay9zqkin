class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        n = len(coins)

        m = amount

        dp = [[0 for _ in range (n)] for _ in range (m+1)]

        for i in range (n):

            dp[0][i] = 1
            
        for a in range (1, m+1):

            for j in range (n):

                if j > 0:
                    
                    dp[a][j] += dp[a][j-1]

                if a-coins[j] >= 0:

                    dp[a][j] += dp[a-coins[j]][j]

        return dp[amount][n-1]

                



                    














        