class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if not tokens:
            return
        if len(tokens) == 1:
            return int(tokens[0])
        stack = []
        i = 0
        operators = ["+", "-", "*", "/"]

        while i < len(tokens):
            while i < len(tokens) and tokens[i] not in operators:
                stack.append(tokens[i])
                i += 1
            num2 = int(stack.pop())
            num1 = int(stack.pop())

            if tokens[i] == "+":
                res = num1 + num2
            elif tokens[i] == "-":
                res = num1 - num2
            elif tokens[i] == "*":
                res = num1 * num2
            elif tokens[i] == "/":
                if num2 == 0:
                    return
                res = float(num1) / float(num2)  # IMPORTANT
            stack.append(res)
            i += 1
        return int(stack.pop())
