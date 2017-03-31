class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n = len(nums2)

        if m > n:
            m, n, nums1, nums2 = n, m, nums2, nums1

        imin = 0
        imax = m

        while imin <= imax:
            i = (imin + imax) // 2
            if (m + n) % 2 == 1:
                # odd length so add 1
                j = (m + n + 1) // 2 - i
            else:
                j = (m + n) // 2 - i

            if i > 0 and nums1[i - 1] > nums2[j]:
                # i too big, reduce i
                imax = i - 1
            elif i < m and nums2[j - 1] > nums1[i]:
                # i too small, increase i
                imin = i + 1
            else:
                # i is correct

                # edge cases
                if i == 0:
                    max_left = nums2[j - 1]
                elif j == 0:
                    max_left = nums1[i - 1]
                else:
                    max_left = max(nums1[i - 1], nums2[j - 1])

                if (m + n) % 2 == 1:
                    return max_left

                if i == m:
                    min_right = nums2[j]
                elif j == n:
                    min_right = nums1[i]
                else:
                    min_right = min(nums1[i], nums2[j])

                return (max_left + min_right) * 0.5


