class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        digits = []
        letters = []
        for log in logs:
            for char in range(len(log)):
                if log[char] == ' ':
                    contents = log[char + 1 : len(log)]
                    identifier = log[0 : char]
                    if ord(contents[0]) - ord('0') >= 0 and ord(contents[0]) - ord('0') <= 9:
                        digits.append(log)
                    else:
                        letters.append((contents, identifier))
                    break
        # now we need to sort the letters map
        # use a minHeap for the letters contents
        heapq.heapify(letters)
        ans = []
        while letters:
            elem = heapq.heappop(letters)
            ans.append(elem[1] + ' ' + elem[0])
        # just add on digits since we need to maintain their relative ordering
        ans.extend(digits)
        return ans