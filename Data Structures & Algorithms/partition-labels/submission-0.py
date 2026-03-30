class Solution:
    def partitionLabels(self, s: str) -> List[int]:

        counter = defaultdict(int)

        seen = set()

        for letter in s:

            counter[letter] += 1

        ret = []

        count = 0

        substringLen = 1

        for letter in s:

            if letter not in seen:

                count += counter[letter]

                seen.add(letter)

            count -= 1
            
            if count == 0:

                ret.append(substringLen)

                substringLen = 1
            
            else:

                substringLen += 1
        
        return ret







        
        