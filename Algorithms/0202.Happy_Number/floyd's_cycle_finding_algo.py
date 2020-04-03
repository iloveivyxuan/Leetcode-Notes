class Solution:
    def isHappy(self, n: int) -> bool:
        def get_next(number):
            sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                sum += digit ** 2
            return sum

        turtle = n
        rabbit = get_next(n)
        while rabbit != 1 and turtle != rabbit:
            turtle = get_next(turtle)
            rabbit = get_next(get_next(rabbit))
        return rabbit == 1
