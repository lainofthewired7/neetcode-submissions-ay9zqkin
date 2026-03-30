import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        heap = stones

        heapq.heapify_max(heap)

        while len(heap) > 1:

            temp1 = heapq.heappop_max(heap)

            temp2 = heapq.heappop_max(heap)

            print(temp1)

            print(temp2)

            if temp1 == temp2:
                
                continue

            else:

                res = abs(temp1 - temp2)

            heapq.heappush_max(heap, res)

        return 0 if not heap else heap[0]
