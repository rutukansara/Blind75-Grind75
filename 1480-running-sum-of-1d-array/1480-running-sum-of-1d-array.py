class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        runningsum = []
        currentsum = 0

        for i in range(len(nums)):
            currentsum += nums[i]
            runningsum.append(currentsum)
        return runningsum
