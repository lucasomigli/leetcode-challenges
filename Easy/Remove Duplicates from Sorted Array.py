class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) < 1:
            return len(nums)
        stack = nums[0]
        index = 0
        for i in nums:
            if i != stack:
                stack = i
                index += 1
                nums.insert(index, stack)
        return index + 1
