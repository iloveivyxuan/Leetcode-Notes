class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = 0
        i = j = 0
        while j < len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
            else:
                zero_count += 1
            j += 1

        nums[i:] = [0] * (len(nums) - i)
