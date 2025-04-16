class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        word_freq = {}
        for word in words:
            word_freq[word] = word_freq.get(word, 0) + 1

        heap = []
        for word, freq in word_freq.items():
            heapq.heappush(heap, (-freq, word))

        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans
