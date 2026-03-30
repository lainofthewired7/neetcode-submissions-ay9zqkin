class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        #union find

        par = [i for i in range (n)] #every node starts off as its own parent

        rank = [1] * n #every node starts as rank 1 since only one node in union

        def find(n1):

            res = n1

            while res != par[res]:

                par[res] = par[par[res]] #path compression

                res = par[res] #continually finding parents

            return res


        def union (n1, n2):

            p1, p2 = find(n1), find(n2)

            if p1 == p2:

                return 0 #did not perform union

            if rank[p2] > rank[p1]:

                par[p1] = p2

                rank[p2] += rank[p1]

            else:

                par[p2] = p1

                rank[p1] += rank[p2]


            return 1

        res = n

        for n1, n2 in edges:

            res -= union(n1, n2)

        return res

            

            


        