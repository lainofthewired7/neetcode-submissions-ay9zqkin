class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        n = len(s2)

        m = len(s1)

        if n + m != len(s3):

            return False

        if not s3:

            return True

        if not s2:

            return s1 == s3
        
        if not s1:

            return s2 == s3

        memo = {}

        def dfs(s1idx, s2idx):

            if (s1idx, s2idx) in memo:

                return memo[(s1idx, s2idx)]

            if s1idx + s2idx + 2 == len(s3):

                return True

            

            k = s1idx + s2idx
            
            if s1idx < len(s1) and s2idx < len(s2) and s3[k] == s1[s1idx] and s3[k] == s2[s2idx]:

                memo[(s1idx, s2idx)] = dfs(s1idx+1, s2idx) or dfs(s1idx, s2idx+1)

            elif s1idx < len(s1) and s3[k] == s1[s1idx]:

                memo[(s1idx, s2idx)] = dfs(s1idx+1, s2idx)

            elif s2idx < len(s2) and s3[k] == s2[s2idx]:

                memo[(s1idx, s2idx)] = dfs(s1idx, s2idx+1)

            else:

                memo[(s1idx, s2idx)] = False

            return memo[(s1idx, s2idx)]

        return dfs(0, 0)
        
        