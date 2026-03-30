class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap = []

        heapq.heapify(heap)

        for x, y in points:

            distance = -pow((x**2 + y**2), 0.5)

            heapq.heappush(heap, [distance, x, y])

            if len(heap) > k:

                heapq.heappop(heap)

        ret = []

        for _, x, y in heap:

            ret.append([x, y])

        return ret





        
        