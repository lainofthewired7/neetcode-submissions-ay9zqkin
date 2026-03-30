class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        goal = n-1
        
        currGoal = goal

        for i in range (goal, -1, -1):

            if i + nums[i] >= currGoal:

                currGoal = i

        return currGoal == 0



                

            
        