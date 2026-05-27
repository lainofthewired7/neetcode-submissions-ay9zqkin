class Solution:
    def myPow(self, x: float, n: int) -> float:

        if x == 0:

            return 0

        if n == 0:

            return 1

        def dfs(x, n):
            
            if n == 0:

                return 1

            res = dfs(x, n//2)

            res = res * res

            if n % 2:

                return x * res

            else:
                
                return res

        res = dfs(x, abs(n))

        if n < 0:

            res = 1/res

        return res
            


        