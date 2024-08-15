class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        start = len(s) - 1
        for i in reversed(range(len(s))):
            if s[i] == ' ':
                start -= 1
            else:
                break
        end = start - 1
        for i in reversed(range(start)):
            if s[i] != ' ':
                end -= 1
            else:
                return start - end
        return start - end