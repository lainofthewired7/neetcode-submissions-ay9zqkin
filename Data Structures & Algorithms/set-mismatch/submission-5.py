class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        count = Counter(nums)

        ret = [0, 0]

        for i in range (1, len(nums)+1):

            if count[i] == 2:

                ret[0] = i

            elif count[i] == 0:

                ret[1] = i

        return ret

