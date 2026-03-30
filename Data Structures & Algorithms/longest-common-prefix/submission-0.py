class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        longestPrefix = strs[0]

        strs = sorted(strs, key=len, reverse=True)

        for word in strs:

            while longestPrefix not in word:

                longestPrefix = longestPrefix[:-1]

        return longestPrefix






        