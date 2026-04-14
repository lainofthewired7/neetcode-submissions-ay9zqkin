class Solution:
    def isHappy(self, n: int) -> bool:

        sum = 0

        seen = set()

        while sum != 1:

            strNum = str(n)

            sum = 0

            for num in strNum:

                sum += pow(int(num), 2)

            if sum in seen:

                return False

            seen.add(sum)

            n = sum

        return True

            



        
        