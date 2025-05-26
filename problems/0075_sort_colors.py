# See: https://leetcode.com/problems/sort-colors/
class Solution(object):
    def sortColors(self, nums):
        return self.soln2(nums)
        # return self.soln1(nums)
        
    # attempt with a LC hint
    def soln2(self, nums):
        counts = [0] * 3
        for val in nums:
            counts[val] += 1

        i = j = 0
        while i < len(nums):
            while counts[j] > 0:
                nums[i] = j
                counts[j] -= 1
                i += 1
            j += 1
        return

    # merge sort attempt, didn't work
    def soln1(self, nums):
        n = len(nums)

        def merge(start, end):
            # recursively merge
            if end - start + 1 > 2:
                # split the array. identify the end of the left half and the start of the right half
                leftEnd = (end - start + 1) // 2
                rightStart = leftEnd + 1
                merge(start, leftEnd)
                merge(rightStart, end)

                # merge the sorted halves
                i, j = start, rightStart
                while i <= leftEnd and j <= end:
                    if nums[i] >= nums[j]:
                        nums[i], nums[j] = nums[j], nums[i]
                        i += 1
                        j += 1
                    else:
                        i += 1

            elif end - start + 1 == 2:
                # sort two indices
                if nums[start] > nums[end]:
                    nums[start], nums[end] = nums[end], nums[start]
            return

        merge(0, n-1)
        return