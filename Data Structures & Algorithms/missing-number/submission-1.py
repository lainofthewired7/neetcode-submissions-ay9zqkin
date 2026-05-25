class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n  = len(nums)

        inputt = set()

        for num in nums:

            inputt.add(num)

        for i in range (n+1):

            if i not in inputt:

                return i







            
        
        
            
        