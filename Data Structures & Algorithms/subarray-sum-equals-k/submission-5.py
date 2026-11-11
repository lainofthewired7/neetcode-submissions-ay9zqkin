class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        ret = 0

        prefix = {0 : 1}

        curr = 0

        for num in nums:

            curr += num

            if curr-k in prefix:

                ret += prefix[curr-k]

            if curr in prefix:

                prefix[curr] += 1

            else:

                prefix[curr] = 1
                
        return ret







