class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        # use deque as you need to do both pop and popleft()
        stack = deque()
        i = 0
        while i < len(s):
            if s[i] in "*/":
                operator = "*" if s[i] == "*" else "/"
                num1 = int(stack.pop())
                i += 1
                while s[i] == " ":
                    i += 1
                num = ""
                while i < len(s) and s[i] not in "+-*/ ":
                    num += s[i]
                    i += 1
                num2 = int(num)

                if operator == "*":
                    stack.append(num1 * num2)
                else:
                    stack.append(num1 // num2)
            elif s[i] in "+-":
                stack.append(s[i])
                i += 1
            elif s[i] == " ":
                i += 1
            else:
                num = ""
                while i < len(s) and s[i] not in "+-*/ ":
                    num += s[i]
                    i += 1
                stack.append(num)

        num2 = num1 = last = None
        while len(stack) > 1:
            out = stack.popleft()
            if str(out) in "+-":
                num1 = int(stack.popleft())
                if out == "+":
                    num2 = num1 + num2
                else:
                    num2 = num2 - num1
            else:
                num2 = int(out)

        if len(stack) == 1:
            return int(stack[0])
        else:
            return num2

print(Solution().calculate("3*2+2"))