class Stack:
    def __init__(self):
        self.items = []

    def push(self, data):
        self.items.append(data)

    def pop(self):
        return self.items.pop()

    def isEmpty(self):
        return len(self.items) == 0

    def peek(self):
        return self.items[len(self.items) - 1]

    def pprint(self):
        for i in range(len(self.items)):
            print(self.items[i])
        print("---------")

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if k == len(num):
            return "0"

        nums = list(num)

        stack = Stack()
        i = 0
        while i < len(nums):
            while k > 0 and not stack.isEmpty() and stack.peek() > nums[i]:
                # while the top of the stack is greater than current item,
                # keep popping the stack and reduce k

                stack.pop()  # this is equivalent to removing a digit.
                k -= 1  # since a digit was removed reduce the k count

            stack.push(nums[i])
            i += 1

        while k > 0:
            stack.pop()  # remove any residual items from the stack
            k -= 1

            # pop remaining items from stack

        res = ""
        while not stack.isEmpty():
            res += stack.pop()

        # reverse it as it is popped from a stack
        # so its in the reverse order and has to be reversed to be corrected
        res = res[::-1]

        # remove any trailing zeroes

        i = 0
        print(res)
        while len(res[i:]) >= 1 and res[i] == "0":
            i += 1
        return res[i:] if res[i:] != "" else "0"



