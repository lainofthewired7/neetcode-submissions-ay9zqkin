class Solution:
    def countSubstrings(self, s: str) -> int:

        self.subCount = 0

        def expand(l, r):

            while l <= r and r < len(s) and l >= 0 and s[l] == s[r]:

                l -= 1

                r += 1

                self.subCount += 1

        for i in range (len(s)):

            expand(i, i)

            expand(i, i+1)

        return self.subCount






        

            


        