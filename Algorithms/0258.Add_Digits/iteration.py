class Solution:
    def addDigits(self, num: int) -> int:
        def get_next(num):
            sum = 0
            while num != 0:
                num, digit = divmod(num, 10)
                sum += digit
            return sum

        while num >= 10:
            num = get_next(num)
        return num
