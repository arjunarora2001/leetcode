class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        do a pass of all the intervals
        if we see an interval that has a starting point greater than any interval's starting point and lesser than that interval's ending point, the ending point is the greater of the two ending points
        eg:
        [1,3], [2,6]
        2 >= 1 and 2 <= 3
        new ending point is the greater of 3 and 6
        """
        starts = []
        ends = []
        for start, end in intervals:
            starts.append(start)
            ends.append(end)
        starts.sort()
        ends.sort()
        ans = []
        start = 0
        end = 0
        while start < len(starts) and end < len(ends):
            tmpStart = start + 1
            while end < len(ends) and tmpStart < len(starts) and ends[end] >= starts[tmpStart]:
                tmpStart += 1
                end += 1
            else:
                ans.append([starts[start], ends[end]])
                start = end + 1
                end += 1
        return ans
        # intervalSet = []
        # for interval in range(len(intervals)):
        #     tmp = intervalSet
        #     for i in intervalSet:
        #         if intervals[interval][0] >= i[0] and intervals[interval][0] <= i[0]:
        #             intervalSet[interval][1] = max(i[1], intervals[interval][1])
        #     if tmp == intervalSet:
        #         intervalSet.append(interval)
        # return intervalSet