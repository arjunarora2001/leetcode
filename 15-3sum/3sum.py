class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        do one pass of the array and store all negatives, positives, zeroes         O(n)
        if len(zeroes) >= 3: add [0,0,0] to ans
        if len(zeroes) >= 1:                                                        (O(n))
            go through positives
            if -positives[i] in negatives:
                add [positives[i], 0, -positives[i]] to ans
        
        now we go through tuples in positives
        eg:
        if sum(1,2) in negatives:
            add [1, 2, -sum(1,2)] to ans
        now we go through tupes in negatives
        eg:
        if sum(-1, -1) in positives:
            add [-1, -1, 1sum(-1 - 1)] to ans
        """
        """
        do one pass of the array                                                    (O(n))
        eg: 
        -1: store 1
        0: store 0
        1: store -1
        2: store -2, etc
        then, do a pass of the array with all tuples                                (O(n^2))
        eg: sum(-1, 0) = -1. -1 is in our set, so we return the (-1, 0, 1)
                                                                                    final: O(n^2 + n) = O(n^2)
        """
        positives = []
        negatives = []
        zeroes = []
        for num in nums:
            if num > 0:
                positives.append(num)
            elif num < 0:
                negatives.append(num)
            else:
                zeroes.append(num)
        P = set(positives)
        N = set(negatives)
        ans = set()
        
        if zeroes:
            if len(zeroes) >= 3:
                ans.add((0,0,0))
            if len(N) > len(P):
                for positive in P:
                    if -positive in N:
                        ans.add((positive, 0, -positive))
            else:
                for negative in N:
                    if -negative in P:
                        ans.add((negative, 0, -negative))
        for i in range(len(positives) - 1):
            for j in range(i + 1, len(positives)):
                if i == j:
                    continue
                if -(positives[i] + positives[j]) in N:
                    ans.add(tuple(sorted((positives[i], positives[j], -(positives[i] + positives[j])))))

        for i in range(len(negatives) - 1):
            for j in range(i + 1, len(negatives)):
                if i == j:
                    continue
                if -(negatives[i] + negatives[j]) in P:
                    ans.add(tuple(sorted((negatives[i], negatives[j], -( negatives[i] + negatives[j])))))
        return ans