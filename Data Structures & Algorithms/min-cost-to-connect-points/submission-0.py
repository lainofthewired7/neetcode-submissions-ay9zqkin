class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:

        par = [i for i in range (len(points))]

        rank = [1] * len(points)

        def find(node):

            p = par[node]

            while p != par[p]:

                par[p] = par[par[p]]

                p = par[p]

            return p

        def union(n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:

                return False

            if rank[p1] > rank[p2]:

                par[p2] = p1

                rank[p1] += rank[p2]

            else:
                par[p1] = p2
                rank[p2] += rank[p1]

            return True


        weightedList = []

        for i in range (len(points)):

            for j in range (len(points)):

                if points[i] != points[j]:

                    weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])

                    weightedList.append((weight, i, j))

        weightedList.sort()

        minCost = 0

        for pair in weightedList:

            if union(pair[1], pair[2]):

                minCost += pair[0]

        return minCost

            



        




        