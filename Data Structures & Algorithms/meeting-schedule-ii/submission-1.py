"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        starts = []

        ends = []

        for interval in intervals:

            starts.append(interval.start)

            ends.append(interval.end)

        starts.sort()

        ends.sort()

        print(starts)

        print(ends)

        count = 0

        maxCount = count

        s = 0

        e = 0

        while s < len(starts):

            if starts[s] >= ends[e]:

                count-=1

                e+=1

            count += 1

            maxCount = max(count, maxCount)

            s+=1

        return maxCount






        