class Solution:
    def minDistance(self, word1: str, word2: str) -> int:

        n = len(word1)

        m = len(word2)

        if not word2:

            return n

        if not word1:

            return m

        dp = [[0 for _ in range (n+1)] for _ in range (m+1)]

        for i in range (n):

            dp[m][i] = n - i

        for j in range (m):

            dp[j][n] = m - j

        print(dp)

        for i in range (m-1, -1, -1):

            for j in range (n-1, -1, -1):

                if word1[j] == word2[i]:

                    dp[i][j] = dp[i+1][j+1]

                else:

                    dp[i][j] = min(dp[i+1][j+1], dp[i+1][j], dp[i][j+1]) + 1

        return dp[0][0]

        




        