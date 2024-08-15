class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magDict = dict(Counter(magazine))
        ransomDict = dict(Counter(ransomNote))
        for letter,freq in ransomDict.items():
            if letter not in magDict:
                return False
            elif freq > magDict[letter]:
                return False
        return True