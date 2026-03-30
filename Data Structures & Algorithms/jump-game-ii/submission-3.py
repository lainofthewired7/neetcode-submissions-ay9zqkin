class Solution:
    def jump(self, nums: List[int]) -> int:

        l = r = 0

        minJumps = 0

        goal = len(nums) - 1

        while r < goal:

            maxJumpIndex = 0

            for i in range (l, r+1):

                maxJumpIndex = max(maxJumpIndex, nums[i] + i)

            l = r + 1

            r = maxJumpIndex

            minJumps += 1

        return minJumps
        