class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:

        if len(hand) % groupSize != 0:

            return False

        hand.sort()

        freq = defaultdict(int)

        for val in hand:

            freq[val] += 1

        for card in hand:

            if freq[card] == 0:

                continue

            for j in range (card, card + groupSize):

                freq[j] -= 1

        
        for elem in freq.values():

            if elem != 0:

                return False

        return True




            




        