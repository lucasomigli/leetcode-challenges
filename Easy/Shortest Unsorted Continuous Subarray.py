class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        nums_sorted = sorted(nums)
        a, b = (0, len(nums) - 1)
        while True:
            if a >= len(nums):
                return 0
            elif nums[a] != nums_sorted[a]:
                break
            a += 1

        while True:
            if nums[b] != nums_sorted[b]:
                break
            b -= 1
        return b - a + 1 if (b - a) > 1 else 2
