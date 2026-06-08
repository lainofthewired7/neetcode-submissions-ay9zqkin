class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if len(s) == 1:

            return 1

        count = {}
        
        length = 0

        l = 0

        maxF = 0

        for r in range (len(s)):

            if s[r] in count:

                count[s[r]] += 1

            else:

                count[s[r]] = 1

            maxF = max(maxF, count[s[r]])

            while (r-l+1) - maxF > k:

                count[s[l]] -= 1

                l += 1

            currLength = r - l + 1

            length = max(length, currLength)

        return length








        
        