class Solution:
    def sortVowels(self, s: str) -> str:
        vowelsWeHave = []
        indices = []
        vowels = set(['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'])
        
        for i, char in enumerate(s):
            if char in vowels:
                vowelsWeHave.append(char)
                indices.append(i)
        
        vowelsWeHave.sort()
        # vowelsWeHave = collections.deque(vowelsWeHave)
        
        s = list(s)
        
        for i in indices:
            s[i] = vowelsWeHave.pop(0)
        
        newS = "".join(s)
        return newS