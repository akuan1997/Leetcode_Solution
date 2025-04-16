class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        anagrams = {}
        for word in strs:
            sorted_word = ''.join(sorted(word))
            anagrams[sorted_word] = anagrams.get(sorted_word, []) + [word]
        return list(anagrams.values())
