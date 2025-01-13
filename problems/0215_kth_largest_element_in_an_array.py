# See: https://leetcode.com/problems/kth-largest-element-in-an-array/
import heapq
class Solution(object):
    def findKthLargest(self, nums, k):
        return self.soln3(nums, k)
        # return self.soln2(nums, k)
        # return self.soln1(nums, k)

    # optimized heap solution based on something I found on stack overflow
    def soln3(self, nums, k):
        heap = nums[:k]
        heapq.heapify(heap)
        for n in nums[k:]:
            if n > heap[0]: # O((n-k) * logk)
                heapq.heapreplace(heap, n)
        return heap[0]

    # heap solution for a priority queue
    def soln2(self, nums, k):
        heap = []
        for c in nums:
            heapq.heappush(heap, -1 * c)
        for _ in range(k-1):
            heapq.heappop(heap)
        return -1 * heapq.heappop(heap)

    # the disallowed sorting solution
    def soln1(self, nums, k):
        nums.sort()
        i = len(nums) - k
        return nums[i]
