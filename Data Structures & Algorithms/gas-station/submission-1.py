class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        if sum(cost) > sum(gas):

            return -1

        currGas = 0

        candidate = 0

        for i in range (len(gas)):

            currGas += gas[i]

            currGas -= cost[i]

            if currGas < 0:

                candidate = i + 1

                currGas = 0

        return candidate


        