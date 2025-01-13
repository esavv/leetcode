# See: https://leetcode.com/problems/unique-number-of-occurrences/
class Solution(object):
    def uniqueOccurrences(self, arr):
        unique_ints = {}
        for num in arr:
            if num not in unique_ints:
                unique_ints[num] = 1
            else:
                unique_ints[num] += 1
            
        occurrences = {}
        for num in unique_ints:
            if unique_ints[num] not in occurrences:
                occurrences[unique_ints[num]] = 1
        
        return len(unique_ints) == len(occurrences)
        