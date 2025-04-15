class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        if not s:
            return 0

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        int_max = 2 ** 31 - 1
        int_min = -2 ** 31

        num = 0
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)

                if num * sign > int_max:
                    return int_max
                elif num * sign < int_min:
                    return int_min
            else:
                break

        return num * sign