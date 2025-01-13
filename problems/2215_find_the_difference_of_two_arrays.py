# See: https://leetcode.com/problems/find-the-difference-of-two-arrays/
class Solution(object):
    def findDifference(self, nums1, nums2):
        return self.soln4(nums1, nums2)
        # return self.soln3(nums1, nums2)
        # return self.soln2(nums1, nums2)
        # return self.soln1(nums1, nums2)

    # hash / set approach #2
    def soln4(self, nums1, nums2):
        answer1, answer2 = [], []
        set1, set2 = set(nums1), set(nums2)
        answer1 = [c for c in set1 if c not in set2]
        answer2 = [c for c in set2 if c not in set1]
        return [answer1, answer2]

    # vector fun
    def soln3(self, nums1, nums2):
        answer1, answer2 = [], []

        mark1 = [0] * 2001
        mark2 = [0] * 2001
        for c in nums1:
            mark1[c+1000] = 1
        for c in nums2:
            mark2[c+1000] = 1

        for c in nums1:
            if mark1[c+1000] == 1 and mark2[c+1000] != 1:
                answer1.append(c)
                mark1[c+1000] = 0
        for c in nums2:
            if mark2[c+1000] == 1 and mark1[c+1000] != 1:
                answer2.append(c)
                mark2[c+1000] = 0

        return [answer1, answer2]

    # hash / set approach #1
    def soln2(self, nums1, nums2):
        answer1, answer2 = [], []

        set1, set2 = {}, {}
        for i, c in enumerate(nums1):
            set1[c] = i 
        for i, c in enumerate(nums2):
            set2[c] = i

        for c in set1:
            if c not in set2:
                answer1.append(c)
        for c in set2:
            if c not in set1:
                answer2.append(c)
        
        return [answer1, answer2]

    # naive approach
    def soln1(self, nums1, nums2):
        answer1 = []
        for c in nums1:
            if c not in nums2 and c not in answer1:
                answer1.append(c)

        answer2 = []
        for c in nums2:
            if c not in nums1 and c not in answer2:
                answer2.append(c)

        return [answer1, answer2]