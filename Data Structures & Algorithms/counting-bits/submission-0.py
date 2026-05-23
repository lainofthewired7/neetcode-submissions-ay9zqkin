class Solution:
    def countBits(self, n: int) -> List[int]:

        ret = []

        for i in range (n+1):

            count = 0

            for j in range (10):

                bitmask = 1 << j

                if (bitmask & i):

                    count += 1

            ret.append(count)

        return ret



            
        