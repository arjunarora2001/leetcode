class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        """
        iterate n times
        check corresponding cells
        if a row does not change from one day to the next, return
        find out if there is a repeating pattern
        """
        patterns = []
        start = 0
        size = len(cells)
        if cells[0] == 1 or cells[-1] == 1:
            start = 1
            ans = [0] * size
            for i in range(1, size - 1):
                ans[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = ans
        for i in range(start, n):
            ans = [0] * size
            for i in range(1, size - 1):
                ans[i] = 1 if cells[i - 1] == cells[i + 1] else 0
            cells = ans
            if patterns and cells == patterns[0]:
                return patterns[(n - start) % len(patterns) - 1]
            patterns.append(ans)
        return cells

        # for i in range(n):
        #     row = cells.copy()
        #     for cell in range(1, len(cells) - 1):
        #         if (cells[cell - 1] in (0, -1) and cells[cell + 1] in (0, -1)) or (cells[cell - 1] in (1, -2) and cells[cell + 1] in (1, -2)):
        #             if cells[cell] == 0:
        #                 cells[cell] = -1 # temporary change to indicate it was vacant but will soon be occupied
        #         else:
        #             cells[cell] = -2 # temporary change to indicate it was occupied but will soon be vacant
        #     if cells == row:
        #         return cells
        #     for cell in range(len(cells)):
        #         if cells[cell] == -1:
        #             cells[cell] = 1
        #         if cells[cell] == -2:
        #             cells[cell] = 0
        #     if patterns and cells == patterns[0]:
        #         return patterns[n % len(patterns) - 1]
        #     patterns.append(cells)
        # return cells