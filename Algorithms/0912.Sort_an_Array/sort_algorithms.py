import heapq

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # self.insertion_sort(nums)
        self.merge_sort(nums)
        return nums

    # @insertion_sort, TLE
    def insertion_sort(self, nums):
        for i in range(1, len(nums)):
            key = nums[i]
            j = i - 1
            while j >= 0 and nums[j] > key:
                nums[j + 1] = nums[j]
                j -= 1
            nums[j + 1] = key
        return nums

    # merge_sort
    def merge_sort(self, nums):
        if len(nums) > 1:
            mid = len(nums) // 2
            left_nums = nums[:mid]
            right_nums = nums[mid:]
            left = self.merge_sort(left_nums)
            right = self.merge_sort(right_nums)

            i = j = k = 0
            while i < len(left_nums) and j < len(right_nums):
                if left_nums[i] < right_nums[j]:
                    nums[k] = left_nums[i]
                    i += 1
                    k += 1
                else:
                    nums[k] = right_nums[j]
                    j += 1
                    k += 1

            while i < len(left_nums):
                nums[k] = left_nums[i]
                i += 1
                k += 1

            while j < len(right_nums):
                nums[k] = right_nums[j]
                j += 1
                k += 1

        return nums

    #heap_sort by using heapq library
    def heap_sort_lib(self, nums):
        res = []
        heapq.heapify(nums)

        for i in range(len(nums)):
            res.append(heapq.heappop(nums))
        return res

    def heap_sort(self, nums):

        def heapify(nums, n, i):
            largest = i
            left = i * 2 + 1
            right = i * 2 + 2

            if left < n and nums[largest] < nums[left]:
                largest = left
            if right < n and nums[largest] < nums[right]:
                largest = right
            if largest != i:
                nums[i], nums[largest] = nums[largest], nums[i]
                heapify(nums, n, largest)

        # Build max_heap
        n = len(nums)
        for i in range(n//2, -1, -1):
            heapify(nums, n, i)

        # sort array in ascending order
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            heapify(nums, i, 0)

        return nums
