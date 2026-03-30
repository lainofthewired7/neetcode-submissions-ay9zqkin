class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        maxLenSubstring = 0

        l = 0

        freq = {}

        maxF = 0 #keep maxF since it wont change and avoid having to loop over freqMap
        #for max everytime

        for r in range (len(s)):

            substringLen = r - l + 1

            if s[r] in freq:

                freq[s[r]] += 1

            else:

                freq[s[r]] = 1

            maxF = max(maxF, freq[s[r]])

            while substringLen - maxF > k:

                freq[s[l]] -= 1

                l += 1

                substringLen -= 1


            maxLenSubstring = max(maxLenSubstring, substringLen)

        return maxLenSubstring





            





        


        