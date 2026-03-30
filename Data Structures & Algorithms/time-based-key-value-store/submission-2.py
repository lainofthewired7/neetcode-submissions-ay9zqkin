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

        closestTimestamp = -1

        if key not in self.map:

            return ""

        for i in self.map[key]:

            if i[1] <= timestamp:

                closestTimestamp = max(closestTimestamp, i[1])

        for i in self.map[key]:

            if i[1] == closestTimestamp:

                return i[0]

        
        return ""
        
