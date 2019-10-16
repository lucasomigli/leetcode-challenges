class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return -2147483648
        maxRun = nums[0]
        hashTable = {0: nums[0]}

        for i in range(1, len(nums)):
            summation = hashTable[i-1] + nums[i]
            hashTable[i] = summation if summation > nums[i] else nums[i]
            maxRun = max(hashTable[i], maxRun, nums[0])
        return maxRun
