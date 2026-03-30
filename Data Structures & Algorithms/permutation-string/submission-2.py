class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        if len(s1) > len(s2):
            
            return False

        s1hash = {}

        s2hash = {}

        l = 0

        for i in s1:

            if i in s1hash:

                s1hash[i] += 1

            else:

                s1hash[i] = 1

        for r in range (len(s2)):

            if s2[r] in s2hash:

                s2hash[s2[r]] += 1

            else:

                s2hash[s2[r]] = 1

            substringLen = r - l + 1

            while r-l + 1 > len(s1):

                if s2hash[s2[l]] == 1:

                    del s2hash[s2[l]]

                else:

                    s2hash[s2[l]] -= 1

                l += 1

            if s1hash == s2hash:

                return True

        return False

        
            






        

        
        