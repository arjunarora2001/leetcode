class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        size = len(s1)
        counter = dict(Counter(s1))
        # print(counter)
        for i in range(len(s2) - size + 1):
            # print(dict(Counter(s2[i:i+size])))
            if dict(Counter(s2[i:i+size])) == counter:
                return True
        return False