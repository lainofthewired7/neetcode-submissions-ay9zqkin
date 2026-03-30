class TimeMap:

    def __init__(self):

        self.map = {}

        self.timeStack = []


    def set(self, key: str, value: str, timestamp: int) -> None:

        if key in self.map:

            self.map[key].append((value, timestamp))

        else:
            
            self.map[key] = [(value, timestamp)]
            

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:

            return ""

        l = 0

        r = len(self.map[key]) - 1

        while l <= r:

            mid = (l+r)//2

            if self.map[key][mid][1] == timestamp:

                return self.map[key][mid][0]

            elif self.map[key][mid][1] > timestamp:

                r = mid - 1

            else:

                l = mid + 1

        
        if self.map[key][mid][1] <= timestamp:

            return self.map[key][mid][0]
        
        elif self.map[key][mid-1][1] <= timestamp:

            return self.map[key][mid-1][0]


        else:
            
            return ""


        
        
        
