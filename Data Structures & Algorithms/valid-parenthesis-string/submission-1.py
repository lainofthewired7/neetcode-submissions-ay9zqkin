class Solution:
    def checkValidString(self, s: str) -> bool:

        leftParIndicies = []

        starIndicies = []

        mistakes = 0

        for i in range (len(s)):

            if s[i] == "*":

                starIndicies.append(i)

            elif s[i] == "(":

                leftParIndicies.append(i)

            else:

                if not starIndicies and not leftParIndicies:

                    return False

                elif leftParIndicies:

                    leftParIndicies.pop()

                else:

                    starIndicies.pop()


        while starIndicies and leftParIndicies:

            if starIndicies.pop() > leftParIndicies[-1]:
                
                leftParIndicies.pop()

        return len(leftParIndicies) == 0










            
        