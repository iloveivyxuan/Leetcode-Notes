# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        peak = 0
        lo, hi = 0, mountain_arr.length() - 1

        while lo < hi:
            midpoint = (lo + hi) // 2
            if mountain_arr.get(midpoint) < mountain_arr.get(midpoint + 1):
                lo = midpoint + 1
            else:
                hi = midpoint
        peak = lo

        lo, hi = 0, peak
        while lo <= hi:
            midpoint = (lo + hi) // 2
            if mountain_arr.get(midpoint) < target:
                lo = midpoint + 1
            elif mountain_arr.get(midpoint) > target:
                hi = midpoint - 1
            else:
                return midpoint

        lo, hi = peak, mountain_arr.length() - 1
        while lo <= hi:
            midpoint = (lo + hi) // 2
            if mountain_arr.get(midpoint) < target:
                hi = midpoint - 1
            elif mountain_arr.get(midpoint) > target:
                lo = midpoint + 1
            else:
                return midpoint

        return -1
