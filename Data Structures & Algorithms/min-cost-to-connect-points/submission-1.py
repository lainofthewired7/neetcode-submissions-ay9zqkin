class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        n = len(points)

        adj = {i:[] for i in range (n)}

        for i in range (len(points)):

            for j in range (len(points)):

                if points[i] != points[j]:

                    adj[i].append((j))


        visited = set()

        minHeap = [(0, 0)]

        minCost = 0 

        while len(visited) != n:

            weight, nodeIndex = heapq.heappop(minHeap)

            if nodeIndex in visited:

                continue

            minCost += weight

            for neiIndex in adj[nodeIndex]:

                weight = abs(points[nodeIndex][0] - points[neiIndex][0]) + abs(points[nodeIndex][1] - points[neiIndex][1])

                heapq.heappush(minHeap, (weight, neiIndex))

            visited.add(nodeIndex)

        return minCost

            

                

            

            

            

        




        