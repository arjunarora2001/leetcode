class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        maxHeap = [ [-freq, char] for char, freq in count.items()]
        heapq.heapify(maxHeap)

        prev = None
        ans = ""

        while maxHeap or prev:
            if not maxHeap and prev:
                return ""
            freq, char = heapq.heappop(maxHeap)
            ans += char
            freq += 1
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None
            if freq < 0:
                prev = [freq, char]
        return ans