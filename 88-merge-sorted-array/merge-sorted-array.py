class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n > 0:
            for i in range(n):
                nums1[i] = nums2[i]
            # nums1 = nums2
            return
        if m > 0 and n == 0:
            return
        p1 = m - 1 # 2
        p2 = n - 1 # 2
        p = len(nums1) - 1 # 5
        while p2 >= 0:
            if nums1[p1] <= nums2[p2]:
                nums1[p] = nums2[p2]
                p2 -= 1
                p -= 1
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                if p1 - 1 < 0:
                    nums1[p1] = nums2[p2]
                    p -= 1
                    while p2 >= 0:
                        nums1[p] = nums2[p2]
                        p -=1
                        p2 -= 1
                    return
                # nums1[p1] = nums1[p1 - 1]
                p -= 1
                p1 -= 1