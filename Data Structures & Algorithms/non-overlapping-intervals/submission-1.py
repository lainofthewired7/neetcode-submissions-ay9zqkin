class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:

        intervals.sort(key = lambda x: x[0])

        if not intervals:

            return 0

        prevEnd = intervals[0][1]

        deletionsNeeded = 0

        for i in range (1, len(intervals)):

            if prevEnd > intervals[i][0]:

                deletionsNeeded += 1

                prevEnd = min(intervals[i][1], prevEnd)

            else:

                prevEnd = intervals[i][1]
            

        return deletionsNeeded








        

       

      
        