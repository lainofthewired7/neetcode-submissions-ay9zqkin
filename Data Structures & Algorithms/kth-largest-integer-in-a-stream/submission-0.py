class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.heap = nums

        self.size = len(self.heap)

        self.k = k
        
    def add(self, val: int) -> int:

        self.heap.append(val)

        self.size += 1

        self.heap.sort()

        return self.heap[self.size - self.k]


        
