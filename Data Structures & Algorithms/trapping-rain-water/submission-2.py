class Solution:
    def trap(self, height: List[int]) -> int:

        prefix = []

        suffix = []

        ret = 0

        for i in range(len(height)):

            if not prefix:

                prefix.append(height[i])

            elif prefix[-1] >= height[i]:

                prefix.append(prefix[-1])

            else:
                
                prefix.append(height[i])

        for j in range(len(height)-1, -1, -1):

            if not suffix:

                suffix.append(height[j])

            elif suffix[-1] >= height[j]:

                suffix.append(suffix[-1])

            else:
                
                suffix.append(height[j])

        suffix.reverse()

        for k in range (len(height)):

            ret += (min(suffix[k], prefix[k]) - height[k])

        return ret


        