class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        ends = set("!?',;. ")
        freq = {}
        pointer = 0
        for char in range(len(paragraph)):
            if pointer > char:
                continue
            if paragraph[char] in ends:
                word = paragraph[pointer : char].lower()
                if word in banned:
                    freq[word] = 0
                elif word in freq:
                    freq[word] += 1
                else:
                    freq[word] = 1
                pointer = char + 1
                while pointer < len(paragraph) and paragraph[pointer] in ends:
                    pointer += 1
            elif char == len(paragraph) - 1:
                word = paragraph[pointer::].lower()
                if word not in banned:
                    if word in freq:
                        freq[word] += 1
                    else:
                        freq[word] = 1
                else:
                    freq[word] = 0
        maxWord = ""
        maxFreq = 0
        for word, frequency in freq.items():
            if frequency > maxFreq:
                maxWord = word
                maxFreq = frequency
        return maxWord
        