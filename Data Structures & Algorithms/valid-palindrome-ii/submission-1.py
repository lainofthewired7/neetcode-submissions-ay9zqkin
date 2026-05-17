class Solution:
    def validPalindrome(self, s: str) -> bool:

        def isPalindrome(s):

            l = 0

            r = len(s) -1

            while l < r:

                if s[l] != s[r]:

                    return False

                l += 1

                r -=1

            return True
        
        l = 0

        r = len(s) - 1

        while l < r:

            if s[l] != s[r]:

                return isPalindrome(s[:l] + s[l+1:]) or isPalindrome(s[:r] + s[r+1:])

            l += 1

            r -= 1

        return True

        







            