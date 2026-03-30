class LRUCache:

    def __init__(self, capacity: int):

        self.myDict = {}

        self.LRU = []

        self.size = 0

        self.capacity = capacity


    def get(self, key: int) -> int:

        for i in self.myDict:

            if i == key:

                if key in self.LRU:

                    self.LRU.remove(key)

                self.LRU.append(key)

                return self.myDict[i]

        return -1
        

    def put(self, key: int, value: int) -> None:

        if key not in self.myDict:

            self.size += 1

        self.myDict[key] = value

        if self.size > self.capacity:

            del self.myDict[self.LRU[0]]

            self.LRU.remove(self.LRU[0])

            self.size = self.capacity

        if key in self.LRU:

            self.LRU.remove(key)

        self.LRU.append(key)

            
            
        
