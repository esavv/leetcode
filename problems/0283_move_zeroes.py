# See: https://leetcode.com/problems/move-zeroes/
class Solution(object):
    def moveZeroes(self, nums):
        return self.soln1(nums)    
        #return self.soln2(nums)
        #return self.soln3(nums)

    def soln1(self, nums):
        length = len(nums)
        left = 0
        for right in range(length):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        return        

    # 'move zeros to the back' approach
    def soln2(self, nums):
        length = len(nums)
        i = 0
        for _ in range(length):
            if nums[i] == 0:
                nums.append(0)
                nums.remove(nums[i])
            else:
                i += 1
        return
        
    # using extra space
    def soln3(self, nums):
        zeros = []
        notzs = []
        for x in nums:
            if x == 0:
                zeros.append(x)
            else:
                notzs.append(x)
        temp = notzs + zeros

        for i, x in enumerate(temp):
            nums[i] = x
