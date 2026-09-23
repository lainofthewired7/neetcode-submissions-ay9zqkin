class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        flowerbed = [0] + flowerbed + [0]

        l, mid, r = 0, 1, 2

        count = 0

        while r < len(flowerbed):

            if flowerbed[l] == flowerbed[mid] == flowerbed[r] == 0:

                count+=1

                flowerbed[mid] = 1

            l += 1

            r += 1

            mid += 1

        return count >= n
        