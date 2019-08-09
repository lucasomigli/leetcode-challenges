class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        stack = []
        for n in range(len(nums)):
            if nums[n] == target:
                stack.append(n)

        first = stack[0] if len(stack) > 0 else -1
        last = stack.pop() if len(stack) > 0 else -1

        return [first, last]
