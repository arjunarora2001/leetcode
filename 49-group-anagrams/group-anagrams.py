class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        for i in strs:
            temp = str(sorted(i))
            if temp not in d.keys():
                d[temp] = []
            d[temp].append(i)
        return d.values()
