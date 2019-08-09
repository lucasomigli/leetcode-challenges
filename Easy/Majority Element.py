class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stack = {}
        for i in range(len(nums)):
            if nums[i] not in stack:
                stack[nums[i]] = 1
            else:
                stack[nums[i]] += 1
            if stack[nums[i]] > len(nums)/2:
                return nums[i]
