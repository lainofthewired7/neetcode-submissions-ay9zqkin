class Solution:
    def longestPalindrome(self, s: str) -> str:

        longest = s[0]

        def expand(l, r):

            while l >= 0 and r < len(s) and s[l] == s[r]:

                l -= 1

                r += 1

            return s[l+1:r]

        for i in range (len(s)):

            p1 = expand(i, i)

            p2 = expand(i, i+1)

            longest = max(longest, p1, p2, key=len)

        return longest

                

                


           



          

        