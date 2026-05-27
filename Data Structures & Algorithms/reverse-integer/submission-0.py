class Solution:
    def reverse(self, x: int) -> int:

        string = str(abs(x))

        newString = ""

        for i in range (len(string)-1, -1, -1):

            newString += string[i]

        ret = int(newString)

        negRet = -int(newString)

        print(ret)

        print(negRet)

        if ret > pow(2, 31) - 1 or negRet < -pow(2, 31):

            return 0

        if x < 0:

            return negRet

        else:

            return ret

        
        