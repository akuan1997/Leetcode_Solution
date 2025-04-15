class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False

        word2char = {}
        char2word = {}

        for word, char in zip(words, pattern):
            if word in word2char:
                if word2char[word] != char:
                    return False
            if char in char2word:
                if char2word[char] != word:
                    return False
            word2char[word] = char
            char2word[char] = word

        return True