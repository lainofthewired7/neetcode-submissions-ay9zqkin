import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l, r = 1, max(piles)

        minK = r

        while l <= r:

            mid = (l+r) // 2

            usedHours = 0

            for i in piles:

                usedHours += math.ceil(i/mid)

            if usedHours > h:

                l = mid + 1

            else:

                minK = min(minK, mid)

                r = mid - 1


        return minK

                





        
         





        