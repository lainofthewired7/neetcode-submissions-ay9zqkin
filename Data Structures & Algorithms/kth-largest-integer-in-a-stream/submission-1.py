class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.heap = []

        self.size = 0

        self.capacity = k

        for num in nums:

            self.heap.append(num)

            self.size += 1

            index = self.size - 1

            while index > 0 and self.heap[index-1] > self.heap[index]:

                self.heap[index-1], self.heap[index] = self.heap[index], self.heap[index-1]

                index -= 1

            if self.size > self.capacity:

                self.heap.pop(0)

                self.size -= 1


        
    def add(self, val: int) -> int:

        self.heap.append(val)

        self.size+=1

        index = self.size - 1

        while index > 0 and self.heap[index-1] > self.heap[index]:

                self.heap[index-1], self.heap[index] = self.heap[index], self.heap[index-1]

                index -= 1

        if self.size > self.capacity:

            self.heap.pop(0)

            self.size -=1

        return self.heap[0]

        
