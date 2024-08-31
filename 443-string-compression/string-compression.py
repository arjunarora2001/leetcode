class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        size = len(chars)
        while i < size:
            char = chars[i]
            count = 0
            while i < size and chars[i] == char:
                i += 1
                count += 1
            chars[index] = char
            index += 1
            if count >= 2:
                strCount = str(count)
                chars[index : index + len(strCount)] = strCount
                index += len(strCount)
        return index