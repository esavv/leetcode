'''
Given a set of numbers and a target number return a count of all the pairs (X,Y)  which sum to the target number.
'''

# The solution I submitted

def countValidPairs(numSet, target):
    if len(numSet) < 2:
        return -1

    pairCount = 0
    for val in numSet:
        complement = target - val
        if complement in numSet and complement > val:
            pairCount += 1

    return pairCount

'''
Given a sorted list L and a target Z return a count of all pairs (X,Y) such that (X+Y)>=Z
'''

# The solution that I didn't get to in time

def countValidPairs(L, Z):
    if len(L) < 2:
        return -1
    
    count = 0
    left, right = 0, len(L)-1
    while left < right:
        # if the current pair meets the condition, we know all vals to the right of left with the current right will also meet the condition
        # after counting those pairs, decrement right to see how many pairs we can form with it
        if L[left] + L[right] >= Z:
            count += right - left
            right -= 1
        else:
            left += 1
    return count