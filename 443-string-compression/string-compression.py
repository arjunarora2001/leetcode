class Solution:
    def compress(self, chars: List[str]) -> int:
        i = 0
        index = 0
        while i < len(chars):
            char = chars[i]
            count = 0
            while i < len(chars) and chars[i] == char:
                i += 1
                count += 1
            chars[index] = char
            index += 1
            if count >= 2:
                for j in str(count):
                    chars[index] = j
                    index += 1
        return index