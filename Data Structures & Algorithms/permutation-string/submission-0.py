class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        s1hash = {}

        s2hash = {}

        l = 0

        for i in s1:

            if i in s1hash:

                s1hash[i] += 1

            else:

                s1hash[i] = 1

        for r in range (len(s2)):

            substringLen = r - l + 1

            while substringLen > len(s1):

                if s2hash[s2[l]] == 1:

                    del s2hash[s2[l]]

                else:

                    s2hash[s2[l]] -= 1

                l += 1

                substringLen -= 1

            if s2[r] in s2hash:

                s2hash[s2[r]] += 1

            else:

                s2hash[s2[r]] = 1

            if s1hash == s2hash:

                return True

            substringLen += 1

        print(s2hash.items())

        print(s1hash.items())

        return False

        
            






        

        
        