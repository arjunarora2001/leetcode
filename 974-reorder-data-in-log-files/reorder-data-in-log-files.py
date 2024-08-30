class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        """
        do a singular pass through logs and categorize them into digit logs and letter logs
        have two hashMaps: one for digit logs and one for letter logs
        find first space
        if first character after space is a number, it's a digit log. else, it's a letter log.
        """
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
                        # letters[identifier] = contents
                    break
        # now we need to sort the letters map
        # maybe use a minHeap for the letters contents?
        # print(letters)
        heapq.heapify(letters)
        # print(letters)
        ans = []
        while letters:
            elem = heapq.heappop(letters)
            elemStr = ""
            elemStr += elem[1]
            elemStr += ' '
            elemStr += elem[0]
            ans.append(elemStr)
        for i in digits:
            ans.append(i)
        return ans