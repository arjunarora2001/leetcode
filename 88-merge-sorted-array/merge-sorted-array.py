class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if m == 0 and n > 0:
            for i in range(n):
                nums1[i] = nums2[i]
            return
        if m > 0 and n == 0:
            return
        
        p = m + n - 1
        m -= 1
        n -= 1
        while n >= 0:
            if nums1[m] <= nums2[n]:
                nums1[p] = nums2[n]
                n -= 1
                p -= 1
            else:
                nums1[p] = nums1[m]
                if m - 1 < 0:
                    nums1[m] = nums2[n]
                    p -= 1
                    while n >= 0:
                        nums1[p] = nums2[n]
                        p -=1
                        n -= 1
                    return
                p -= 1
                m -= 1