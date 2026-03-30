class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:

        fleets = []

        sortedPosition = sorted(position, reverse=True)

        for i in sortedPosition:

            time = (target - i) / speed[position.index(i)]

            if not fleets:

                fleets.append(time)

            else:

                if fleets[-1] < time:

                    fleets.append(time)


        return len(fleets)






        



        

        
        