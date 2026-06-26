class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        stack = []

        for roid in asteroids:

            addition = True

            while stack and (stack[-1] > 0 and roid < 0):

                if abs(stack[-1]) < abs(roid):
                    
                    stack.pop()

                elif abs(stack[-1]) == abs(roid):

                    stack.pop()

                    addition = False

                    break

                else:

                    addition = False

                    break

            if addition:

                stack.append(roid)

        return stack

            


            

