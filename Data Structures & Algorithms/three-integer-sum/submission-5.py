class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums = sorted(nums)

        ret = []

        for i in range (len(nums)-2):

            j = i+1

            k = len(nums) - 1

            target = -nums[i]

            while k > j:

                if nums[j] + nums[k] == target:

                    if [nums[i], nums[j], nums[k]] not in ret:

                        ret.append([nums[i], nums[j], nums[k]])

                    j+=1

    
                elif nums[j] + nums[k] > target:

                    k-=1

                else:

                    j+=1

        return ret

                    








