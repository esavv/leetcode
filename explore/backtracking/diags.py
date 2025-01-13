# Backtracking Explore Card: https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/

# print all of the indices along two diagonals from a given index (row, col) in an nXn grid
def diag(n, row, col):
    ## mark the "increasing" diagonals
    hi = n - 1 - max(row, col)
    lo = 0 - min(row, col)
    print("Diagonals for index (" + str(row) + ", " + str(col) + ")")
    print("The increasing diagonals are: ")
    for i in range(lo, hi+1):
        if i == 0:
            continue
        print("  (" + str(row+i) + ", " + str(col+i) + ")")
    ## mark the "decreasing" diagonals
    hi = min(n - 1 - row, col - 0)
    lo = max(0 - row, col - n + 1)
    print("\nThe decreasing diagonals are: ")
    for i in range(lo, hi+1):
        if i == 0:
            continue
        print("  (" + str(row+i) + ", " + str(col-i) + ")")
    return