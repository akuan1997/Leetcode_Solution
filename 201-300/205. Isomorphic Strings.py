class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        s2t = {}
        t2s = {}

        for c1, c2 in zip(s, t):
            if c1 in s2t:
                if s2t[c1] != c2:
                    return False
            elif c2 in t2s:
                if t2s[c2] != c1:
                    return False
            s2t[c1] = c2
            t2s[c2] = c1

        return True