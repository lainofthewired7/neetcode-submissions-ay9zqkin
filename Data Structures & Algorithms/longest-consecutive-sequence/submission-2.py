class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        sortSeq = sorted(nums)

        maxSeq = 0

        if len(nums) == 0:

            return maxSeq

        seq = 1

        for i in range (len(sortSeq)-1):
            
            consecutive = sortSeq[i+1]

            if consecutive == sortSeq[i]:

                continue

            if consecutive == (sortSeq[i] + 1):

                seq+=1

            else:

                if seq > maxSeq:

                    maxSeq = seq

                seq = 1

        if seq > maxSeq:

            maxSeq = seq

            
        return maxSeq

        

        