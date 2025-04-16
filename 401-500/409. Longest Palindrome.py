class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = [0] * 128

        length = 0
        odd_found = False

        for char in s:
            char_count[ord(char)] += 1

        for count in char_count:
            if count % 2 == 0:
                length += count
            else:
                length += count - 1
                odd_found = True

        return length + 1 if odd_found else length