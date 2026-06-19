class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        copy = heights

        copy = sorted(heights)

        copy = list(copy)

        print(heights)

        print(copy)

        counter = 0

        for i in range (len(heights)):

            if copy[i] != heights[i]:
                counter += 1

        return counter
        