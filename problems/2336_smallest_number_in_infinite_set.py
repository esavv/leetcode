# See: https://leetcode.com/problems/smallest-number-in-infinite-set/
class SmallestInfiniteSet(object):
    def __init__(self):
        self.infset = 1
        self.popped = set()

    def popSmallest(self):
        val = self.infset
        i = 1
        while val+i in self.popped:
            i += 1
        self.infset = val + i
        self.popped.add(val)
        return val

    def addBack(self, num):
        if num in self.popped:
            self.infset = min(num, self.infset)
            self.popped.remove(num)
