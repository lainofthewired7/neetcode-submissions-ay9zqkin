class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0

        right = len(numbers) - 1

        answerArray = []

        while left < right:

            if numbers[left] + numbers[right] == target:

                answerArray.append(left+1)
                answerArray.append(right+1)
                break

            elif numbers[left] + numbers[right] < target:

                left = left + 1

            else:

                right = right - 1
        
        return answerArray
        

            

            

            

                




            



            
        