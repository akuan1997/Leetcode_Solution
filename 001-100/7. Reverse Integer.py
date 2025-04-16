class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2 ** 31 - 1
        int_min = -2 ** 31

        sign = 1 if x > 0 else -1
        x = abs(x)

        num = 0
        while x > 0:
            num = num * 10 + x % 10
            x //= 10

        if num * sign > int_max or num * sign < int_min:
            return 0
        else:
            return num * sign