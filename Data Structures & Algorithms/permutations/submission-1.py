class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        length = len(nums)

        sol = []

        ret = []

        def backtrack(used):

            if len(sol) == length:

                ret.append(sol[:])

                return

            for num in nums:

                if num not in used:
                    
                    sol.append(num)

                    used.add(num)

                    backtrack(used)

                    sol.pop()

                    used.remove(num)
        
        backtrack(set())

        return ret



            

            

            

            

            



        
        