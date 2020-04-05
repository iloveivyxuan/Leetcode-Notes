from collections import defaultdict
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        dictionary = defaultdict(int)
        for i in s:
            dictionary[i] += 1

        odd_count = 0
        for i in dictionary:
            if dictionary[i] % 2 != 0:
                odd_count += 1

        return odd_count <= 1
