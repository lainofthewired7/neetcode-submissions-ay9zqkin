class Solution:
    def jump(self, nums: List[int]) -> int:

        l, r = 0, 0

        minJumps = 0

        if len(nums) == 1:

            return 0
        
        goal = len(nums) - 1

        while r < len(nums):

            furthestIndex = -1

            for j in range (l, r+1):

                furthestIndex = max(furthestIndex, j + nums[j])

            if furthestIndex >= goal:

                return minJumps + 1

            r = furthestIndex

            minJumps += 1

        return minJumps


            






        