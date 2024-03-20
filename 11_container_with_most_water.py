class Solution(object):
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0
        while left < right:
            wide = right - left
            lheight, rheight = height[left], height[right]
            high = min(lheight, rheight)
            max_area = max(wide * high, max_area)

            if lheight < rheight:
                while height[left] <= lheight and left < right:
                    left += 1
            else:
                while height[right] <= rheight and left < right:
                    right -= 1
        return max_area
