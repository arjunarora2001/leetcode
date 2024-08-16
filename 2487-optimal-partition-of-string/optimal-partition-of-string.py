class Solution:
    def partitionString(self, s: str) -> int:
        tempSet = set()
        counter = 1
        for i in s:
            if i in tempSet:
                counter += 1
                tempSet = set(i)
            else:
                tempSet.add(i)
        return counter