class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        A = []

        sum = {}

        for i in range (len(nums)):
            difference = target - nums[i]

            if difference in sum:

                A.append(sum[difference])
                A.append(i)
                return A

            else:

                sum[nums[i]] = i

        
        return A

        