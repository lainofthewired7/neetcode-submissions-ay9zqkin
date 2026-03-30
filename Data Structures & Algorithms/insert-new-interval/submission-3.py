class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        if not intervals:

            return [newInterval]

        

        intervals.append(newInterval)

        intervals.sort(key = lambda x: x[0])

        ret = [intervals[0]]

        for i in range (1, len(intervals)):

            if intervals[i][0] > ret[-1][1]:

                ret.append(intervals[i])

            else:

                ret[-1] = [ret[-1][0], max(intervals[i][1], ret[-1][1])]

        return ret
        