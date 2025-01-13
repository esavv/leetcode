# See: https://leetcode.com/problems/search-insert-position/
class Solution(object):
    def searchInsert(self, nums, target):
        return self.soln2(nums, target)
        # return self.soln1(nums, target)
    
    # Same approach but without recursion
    def soln2(self, nums, target):
        start = 0
        end = len(nums) - 1
        length = end - start + 1
        while length > 2:
            middle = (start + end) // 2
            if target == nums[middle]:
                return middle
            elif target < nums[middle]:
                end = middle - 1
            else:
                start = middle + 1
            length = end - start + 1

        if target <= nums[start]:
            return start
        if target <= nums[end]:
            return end
        return end+1

    def soln1(self, nums, target):
        return self.search(nums, target, 0, len(nums)-1)
    
    def search(self, nums, target, start, end):
        length = end - start + 1
        if length <= 2:
            if target <= nums[start]:
                return start
            if target <= nums[end]:
                return end
            return end+1
        
        middle = (start + end) // 2

        if target == nums[middle]:
            return middle
        elif target < nums[middle]:
            return self.search(nums, target, start, middle-1)
        else:
            return self.search(nums, target, middle+1, end)
        