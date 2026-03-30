class Solution:
    def partition(self, s: str) -> List[List[str]]:

        ret = []

        sol = []

        def backtrack(i):
                
            if i == len(s):

                ret.append(sol[:])

                return

            for j in range (i, len(s)):

                isPalindrome = True

                l = i

                r = j

                while l < r:

                    if s[l] != s[r]:

                        isPalindrome = False

                        break

                    l += 1

                    r -= 1

                if isPalindrome:

                    sol.append(s[i:j+1])

                    backtrack(j+1)

                    sol.pop()

        backtrack(0)

        return ret

            
        