class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        output = []

        for i in range(len(nums)):

            j = 0

            product = 1

            while j < len(nums):

                if i is not j:
                    product = product * nums[j]
                
                j+=1

            output.append(product)

        return output











            




    









        