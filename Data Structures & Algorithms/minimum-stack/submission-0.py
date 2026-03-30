class MinStack:

    def __init__(self):

        self.stack = []
        

    def push(self, val: int) -> None:

        self.stack.append(val)
        

    def pop(self) -> None:

        self.stack.pop()
        

    def top(self) -> int:
        
        return self.stack[-1]

    def getMin(self) -> int:

        min = self.stack[-1]

        temp = []

        while self.stack:

            if self.stack[-1] < min:

                temp.append(self.stack.pop())

                min = temp[-1]

            else:

                temp.append(self.stack.pop())

        while temp:

            self.stack.append(temp.pop())

        return min
                
            
        
