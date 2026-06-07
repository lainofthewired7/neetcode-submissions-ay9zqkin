class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        stack = []

        ret = [0] * (len(temperatures))

        for i in range (len(temperatures)):

            if not stack:

                stack.append(i)

            else:

                while stack and temperatures[stack[-1]] < temperatures[i]:

                    index = stack.pop()

                    ret[index] = i - index

                stack.append(i)

        return ret

        



            

            

            

            




        