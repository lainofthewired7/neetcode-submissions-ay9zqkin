class Solution:
    def isPalindrome(self, s: str) -> bool:



        left = 0

        lower = s.lower()

        right = len(lower) - 1

        while left < right:

            while not lower[left].isalnum() and left < right:

                left = left + 1

            while not lower[right].isalnum() and left < right :
                
                right = right - 1
            
            if lower[left] is not lower[right]:
                return False

            left = left + 1

            right = right - 1


        return True



