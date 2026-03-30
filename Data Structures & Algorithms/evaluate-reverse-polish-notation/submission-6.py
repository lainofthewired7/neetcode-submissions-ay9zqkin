class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        RPN = []

        for i in tokens:

            if i not in {"+", "-", "*", "/"}:

                RPN.append(i)

            else:

                if i == "+":

                    a = int(RPN.pop())

                    b = int(RPN.pop())

                    result = b + a

                    RPN.append(str(result))

                elif i == "-":

                    a = int(RPN.pop())

                    b = int(RPN.pop())

                    result = b - a

                    RPN.append(str(result))

                elif i == "*":

                    a = int(RPN.pop())

                    b = int(RPN.pop())

                    result = b * a

                    RPN.append(str(result))

                elif i == "/":

                    a = int(RPN.pop())

                    b = int(RPN.pop())

                    result = int(b / a)

                    RPN.append(str(result))

        return int(RPN[-1])








        