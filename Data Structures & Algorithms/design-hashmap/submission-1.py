class MyHashMap:

    def __init__(self):

        self.arr = []
        
    def put(self, key: int, value: int) -> None:

        for i in range (len(self.arr)):

            if self.arr[i][0] == key:

                self.arr.pop(i)

                self.arr.append((key, value))

                return  

        self.arr.append((key, value))
        

    def get(self, key: int) -> int:

        for tup in self.arr:

            if tup[0] == key:

                return tup[1]

        return -1
        

    def remove(self, key: int) -> None:

        for i in range (len(self.arr)):

            if self.arr[i][0] == key:

                self.arr.pop(i)

                return
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)