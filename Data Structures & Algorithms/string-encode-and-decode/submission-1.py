class Solution:

    def encode(self, strs: List[str]) -> str:


        singleString = []

        for i in strs:

            singleString.append(str(len(i)))

            singleString.append("#")

            singleString.append(i)

            

        encodedString = "".join(singleString)

        return encodedString


    def decode(self, s: str) -> List[str]:

        outputStrings = []

        seperator = []

        outputString = []

        i = 0

        while i < (len(s)):

            if s[i] == "#":

                i = i + 1

                iterator = "".join(seperator)

                seperator = []

                for j in range (int(iterator)):

                    outputString.append(s[i])

                    i = i+1

                outputStrings.append("".join(outputString))

                outputString = []
            
            else:

                seperator.append(s[i])

                i = i + 1

        return outputStrings

        


            




        


