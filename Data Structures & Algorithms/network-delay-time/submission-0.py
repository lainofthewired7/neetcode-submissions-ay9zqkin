class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        delayMinHeap = []

        heapq.heappush(delayMinHeap, (0, k))

        adj = {i:[] for i in range (1, n+1)}

        dist = [float('inf') for i in range (n)]

        dist[k-1] = 0

        for n1, n2, time in times:

            adj[n1].append((n2, time))
        

        while delayMinHeap:
                
            currTime, node = heapq.heappop(delayMinHeap)

            if currTime > dist[node-1]:

                continue

            dist[node-1] = currTime

            for nei, time in adj[node]:

                heapq.heappush(delayMinHeap, (currTime + time, nei))

            

        
        if float('inf') in dist:

            return -1

        else:

            return max(dist)




            



            





    

            


        