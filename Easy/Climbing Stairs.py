class Solution:
    def climbStairs(self, n: int) -> int:
        stack = [1, 2]
        if n == 0 or not stack:
            return 0
        elif n <= 2:
            return stack[n-1]

        for i in range(2, n):
            stack.append(stack[-2] + stack[-1])
            stack.pop(0)

        return stack.pop()
