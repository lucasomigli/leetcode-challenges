class Solution:
    def addDigits(self, num: int) -> int:
        def add_pair(number):
            stack = 0
            for char in str(number):
                stack += int(char)
            return int(stack)
        res = num
        while (len(str(res)) > 1):
            res = add_pair(res)

        return res
