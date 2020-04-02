from collections import defaultdict

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = defaultdict(int)

        for i in nums:
            hash[i] += 1

        for i in hash:
            if hash[i] == 1:
                return i
