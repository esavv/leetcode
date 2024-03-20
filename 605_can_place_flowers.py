# See: 
class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        pre = 0
        openSpots = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and pre == 0 and (i == len(flowerbed) - 1 or flowerbed[i+1] == 0):
                openSpots += 1
                pre = 1
            else:
                pre = flowerbed[i]
            if openSpots >= n:
                return True
        return False
        