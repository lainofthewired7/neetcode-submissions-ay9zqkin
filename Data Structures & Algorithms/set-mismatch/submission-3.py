class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        seen = set()

        missing = 0

        duplicate = 0

        nums.sort()

        for num in nums:

            if num in seen:

                duplicate = num

                break

            else:

                seen.add(num)

        for i in range (1, len(nums)+1):

            if nums[i-1] == i:

                continue

            elif i not in nums:

                missing = i


        return [duplicate, missing]
        