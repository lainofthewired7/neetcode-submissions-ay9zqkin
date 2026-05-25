class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        newList = []

        ret = []

        for num in digits:

            newList.append(str(num))

        plusOne = "".join(newList)

        plusOne = str(int(plusOne) + 1)

        for char in plusOne:
            
            ret.append(int(char))
            
        return ret
            



