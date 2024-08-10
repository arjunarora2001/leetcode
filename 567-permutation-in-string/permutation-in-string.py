class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size1 = len(s1)
        size2 = len(s2)
        if size1 > size2:
            return False
        s1Freq = [0] * 26
        s2Freq = [0] * 26
        for i in range(size1):
            s1Freq[ord(s1[i]) - ord('a')] += 1
            s2Freq[ord(s2[i]) - ord('a')] += 1
        if s1Freq == s2Freq:
            return True
        for i in range(size1, size2):
            s2Freq[ord(s2[i]) - ord('a')] += 1
            s2Freq[ord(s2[i - size1]) - ord('a')] -= 1
            if s1Freq == s2Freq:
                return True
        return False
            