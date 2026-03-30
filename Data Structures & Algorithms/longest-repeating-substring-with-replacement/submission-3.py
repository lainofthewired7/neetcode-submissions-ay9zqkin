class Solution:
    def characterReplacement(self, s: str, k: int) -> int:


        maxLenSubstring = 0

        l = 0

        freq = {}

        for r in range (len(s)):

            substringLen = r - l + 1

            if s[r] in freq:

                freq[s[r]] += 1

            else:

                freq[s[r]] = 1

            while substringLen - max(freq.values()) > k:

                freq[s[l]] -= 1

                l += 1

                substringLen -= 1


            maxLenSubstring = max(maxLenSubstring, substringLen)

        return maxLenSubstring





            





        


        