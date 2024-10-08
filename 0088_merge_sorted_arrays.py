# See: https://leetcode.com/problems/merge-sorted-array/
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        return self.soln1(nums1, m, nums2, n)

    # linear time & space
    def soln1(self, nums1, m, nums2, n):
        if n == 0:
            return

        temp = [0] * (m+n)
        idx1, idx2, idxt = 0, 0, 0
        
        while idx1 < m and idx2 < n:
            if nums1[idx1] <= nums2[idx2]:
                temp[idxt] = nums1[idx1]
                idx1 += 1
                idxt += 1
            else:
                temp[idxt] = nums2[idx2]
                idx2 += 1
                idxt += 1
				
        while idx1 < m:
            temp[idxt] = nums1[idx1]
            idx1 += 1
            idxt += 1

        while idx2 < n:
            temp[idxt] = nums2[idx2]
            idx2 += 1
            idxt += 1

        for idx, num in enumerate(temp):
            nums1[idx] = num
        return
        