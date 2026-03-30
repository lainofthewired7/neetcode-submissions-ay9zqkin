class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:

        minCost = 0

        dist = {}

        adj = {i:[] for i in range (n)}

        for f1, f2, weight in flights:

            adj[f1].append((f2, weight))

        minHeap = [(0, src, 0)]

        while minHeap:

            currCost, n1, stops = heapq.heappop(minHeap)

            if n1 == dst:

                return currCost

            if stops > k:

                continue

            if (n1, stops) in dist:

                if dist[(n1, stops)] < currCost: #how to deal with cycles?

                    continue
                
            else:

                dist[(n1, stops)] = currCost

            
            for n2, cost in adj[n1]:

                heapq.heappush(minHeap, (currCost + cost, n2, stops+1))

        return -1

            



            



            

            
        