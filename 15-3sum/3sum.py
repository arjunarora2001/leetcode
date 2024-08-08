class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        positives = []
        negatives = []
        zeroes = []
        for i in nums:
            if i == 0:
                zeroes.append(i)
            elif i > 0:
                positives.append(i)
            elif i < 0:
                negatives.append(i)
        P = set(positives)
        N = set(negatives)
        if zeroes:
            if len(zeroes) >= 3:
                ans.add((0,0,0))
            for n in N:
                if -1*n in P:
                    ans.add((-1*n, 0, n))
        else:
            if not negatives or not positives:
                return ans
        # for all tuples of negatives, check for the complementary positive
        for i in range(len(negatives) - 1):
            for j in range(i+1, len(negatives)):
                if i == j:
                    continue
                target = -1 * (negatives[i] + negatives[j])
                if target in P:
                    tmp = sorted([negatives[i], negatives[j], target])
                    ans.add(tuple(tmp))

        for i in range(len(positives) - 1):
            for j in range(i+1, len(positives)):
                if i == j:
                    continue
                target = -1*(positives[i] + positives[j])
                if target in N:
                    tmp = sorted([positives[i], positives[j], target])
                    ans.add(tuple(tmp))
        
        return ans