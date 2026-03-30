class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if not s:

            return 0

        maxLength = 1

        l = 0

        seen = set()

        for r in range (len(s)):

            while s[r] in seen:

                seen.remove(s[l])

                l += 1

            seen.add(s[r])

            maxLength = max(maxLength, r - l + 1)

        return maxLength
        