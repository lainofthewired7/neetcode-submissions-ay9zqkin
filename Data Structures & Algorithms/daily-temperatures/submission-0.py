class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        slow = 0

        fast = 1

        ret = []

        while slow < len(temperatures):

            curr = temperatures[slow]

            count = 0

            found = False

            while fast < len(temperatures):

                if curr < temperatures[fast]:

                    count += 1

                    found = True

                    break

                count += 1

                fast += 1

            ret.append(count) if found else ret.append(0)

            slow += 1

            fast = slow + 1

        return ret


                
                



 

        