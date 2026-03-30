class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:

            return 0

        maxLength = 1

        l, r = 0, 1

        seen = set(s[l])

        while r < len(s):

            if s[r] in seen:

                l += 1

                r = l

                seen = set(s[l])
            
            else:

                seen.add(s[r])

                length = (r - l) + 1

                maxLength = max(length, maxLength)

            r += 1
            

        return maxLength
        