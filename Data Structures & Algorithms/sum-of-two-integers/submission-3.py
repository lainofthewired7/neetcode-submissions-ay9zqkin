class Solution:
    def getSum(self, a: int, b: int) -> int:

        res = 0

        remainder = 0

        for i in range (32):

            bitA = 1 & (a >> i)

            bitB = 1 & (b >> i)

            if remainder:

                if bitA and bitB:

                    remainder += 1

                    res |= (1 << i)

                elif bitA or bitB:

                    remainder += 1

                else:
                    
                    res |= (1 << i)


                remainder -= 1

            else:

                if bitA and bitB:

                    remainder = 1

                elif bitA or bitB:

                    res |= (1 << i)


        if res > 2147483647:

            res = ~(res ^ 0xFFFFFFFF)

        return res

            




            

        