class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def get_str(s):
            stack = []
            for char in s:
                if char == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(char)
            return ''.join(stack)

        return get_str(s) == get_str(t)
