class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        stack = []
        length = 0
        for n in range(0, len(nums)):
            if nums[n] == 1:
                stack.append(nums[n])
            else:
                length = len(stack) if len(stack) > length else length
                stack.clear()
        return len(stack) if len(stack) > length else length
