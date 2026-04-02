class Solution:
    def longestPalindrome(self, s: str) -> str:

        n = len(s)

        def helper(s):

            l = 0

            r = len(s) - 1

            while l < r:

                if s[l] != s[r]:

                    return False

                l += 1

                r -= 1

            return True

        dp = [0] * n

        dp[0] = s[0]

        for i in range (1, n):

            dp[i] = s[i]

            for j in range (0, i):

                if helper(s[j:i+1]):

                    dp[i] = s[j:i+1]

                    break

        longest = dp[n-1]

        for j in range (n-1, -1, -1):

            if len(dp[j]) > len(longest):

                longest = dp[j]

        return longest

        


        