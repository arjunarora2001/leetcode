class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        for word in words:
            freq[word] = freq.get(word, 0) + 1
        
        sortedItems = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
        
        return [word for word, _ in sortedItems[:k]]