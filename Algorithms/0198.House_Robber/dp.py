class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        n = len(nums) - 1
        dp[n] = nums[n]
        dp[n-1] = nums[n-1]

        for i in range(n-2, -1, -1):
            dp[i] = nums[i] + max(dp[i+2:])

        return max(dp[0], dp[1])
