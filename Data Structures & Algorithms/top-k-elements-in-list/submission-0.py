class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        A = []


        dict = {}

        for i in nums:
            if i in dict:
                dict[i]+= 1

            else:
                dict[i] = 1

        arr = []

        for num, freq in dict.items():
            arr.append([freq, num])

        arr.sort()

        res = []

        while len(res) < k:
            res.append(arr.pop()[1])

        return res



        
        return A