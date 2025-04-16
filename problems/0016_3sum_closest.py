# See: 
class Solution(object):
    def threeSumClosest(self, nums, target):
        return self.soln2(nums, target)
        # return self.soln1(nums, target)

    # soln #2 on 4/15/2025
    # sorting + two pointers
    def soln2(self, nums, target):
        closestDiff = float("inf")
        closestSum = None

        nums.sort()
        n = len(nums)
        left1, left2, right = 0, 1, n-1
        while right > left2:
            currentSum = nums[left1] + nums[left2] + nums[right]
            currentDiff = target - currentSum
            currentAbsDiff = abs(currentDiff)
            if currentAbsDiff < closestDiff:
                closestDiff = currentAbsDiff
                closestSum = currentSum
            if left2 == right - 1: # check if we need to typewriter reset
                left1, left2, right = left1 + 1, left1 + 2, n-1
            elif currentDiff > 0: # sum is too small, try to make it bigger
                left2 += 1
            elif currentDiff < 0: # sum is too big, try to make it smaller
                right -= 1
            else:
                break # we found the target
        return closestSum    
    
    # soln #1 on 4/15/2025
    # brute force
    def soln1(self, nums, target):
        closestDiff = float("inf")
        closestSum = None
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    currentSum = nums[i] + nums[j] + nums[k]
                    currentDiff = abs(target - currentSum)
                    if currentDiff < closestDiff:
                        closestDiff = currentDiff
                        closestSum = currentSum
        return closestSum