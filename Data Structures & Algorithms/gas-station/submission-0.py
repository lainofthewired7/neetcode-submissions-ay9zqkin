class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if not gas:

            return -1

        loopRange = len(cost) * 2

        candidate = 0

        currGas = 0

        for i in range (loopRange):

            index = i % len(cost)

            if currGas < 0:

                candidate = index

                currGas = 0

            currGas += gas[index]

            currGas -= cost[index]

        currGas = 0

        for i in range (candidate, loopRange):
            
            index = i % len(cost)

            if currGas < 0:

                return -1

            currGas += gas[index]

            currGas -= cost[index]

        return candidate

        