class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        if sorted(list(strs[i])) in dict:
            add strs[i] to dict[strs[i]]
        """
        d = {}
        for s in strs:
            sortedString = sorted(list(s))
            sortedString = str(sortedString)
            if sortedString in d:
                d[sortedString].append(s)
            else:
                d[sortedString] = [s]
        return list(d.values())