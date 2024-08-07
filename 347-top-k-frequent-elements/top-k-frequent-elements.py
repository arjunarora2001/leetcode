class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # print(Counter(nums))
        d = dict(Counter(nums).items())
        sortedDict = dict(sorted(d.items(), key=lambda item: item[1], reverse=True))
        keys = list(sortedDict.keys())
        return keys[:k]