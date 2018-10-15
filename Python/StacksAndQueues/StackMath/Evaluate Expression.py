"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Examples:

  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


class Solution:

    def evaluate_exp(self, data):

        stack = []
        operators = {"/", "+", "*", "-", "%"}

        for item in data:
            if item not in operators:
                stack.append(item)
            else:
                x1 = int(stack.pop())
                x2 = int(stack.pop())
                if item == "+":
                    stack.append(x2 + x1)
                elif item == "-":
                    stack.append(x2 - x1)
                elif item == "*":
                    stack.append(x2 * x1)
                elif item == "/":
                    stack.append(x2 / x1)
                elif item == "%":
                    stack.append(x2 % x1)
        return int(stack[-1])

s = Solution()
ex = ["4", "13", "5", "/", "+"]
print(s.evaluate_exp(ex))