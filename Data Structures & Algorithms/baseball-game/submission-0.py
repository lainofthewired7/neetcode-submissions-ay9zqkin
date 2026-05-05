class Solution:
    def calPoints(self, operations: List[str]) -> int:

        stack = []

        total = 0

        for op in operations:

            if op == "D":

                double = stack[-1]

                double = double * 2

                stack.append(double)

            elif op == "C":

                stack.pop()

            elif op == "+":

                num1, num2 = stack[-1], stack[-2]

                result = int(num1) + int(num2)

                stack.append(result)

            else:

                stack.append(int(op))

        while stack:

            total += stack.pop()

        return total
        