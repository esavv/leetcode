def soln1(n):
    # To manage the queen exploration, initialize an nXn 2d list to 0s
    # -1 represents a queen
    # Positive ints indicate how many queens can attack the space
    grid = [[0 for _ in range(n)] for _ in range(n)]

    def backtrack(row, count):
        for col in range(n):
            if is_not_under_attack(row, col):
                place_queen(row, col)
                if row + 1 == n:
                    count += 1
                else:
                    count = backtrack(row + 1, count)
                remove_queen(row, col)
        return count
    
    def is_not_under_attack(row, col):
        if grid[row][col] == 0:
            return True
        return False

    def place_queen(row, col):
        # first, place the queen
        grid[row][col] = -1

        # then, mark the queen's attack spaces
        ## mark the verticals
        for i in range(n):
            if i == row:
                continue
            grid[i][col] += 1

        ## mark the horizontals
        for i in range(n):
            if i == col:
                continue
            grid[row][i] += 1

        ## mark the "increasing" diagonals
        hi = n - 1 - max(row, col)
        lo = 0 - min(row, col)
        for i in range(lo, hi+1):
            if i == 0:
                continue
            grid[row+i][col+i] += 1

        ## mark the "decreasing" diagonals
        hi = min(n - 1 - row, col - 0)
        lo = max(0 - row, col - n + 1)
        for i in range(lo, hi+1):
            if i == 0:
                continue
            grid[row+i][col-i] += 1
        return

    def remove_queen(row, col):
        # first, remove the queen
        grid[row][col] = 0

        # then, decrement the queen's attack spaces
        ## unmark the verticals
        for i in range(n):
            if i == row:
                continue
            grid[i][col] -= 1

        ## unmark the horizontals
        for i in range(n):
            if i == col:
                continue
            grid[row][i] -= 1

        ## unmark the "increasing" diagonals
        hi = n - 1 - max(row, col)
        lo = 0 - min(row, col)
        for i in range(lo, hi+1):
            if i == 0:
                continue
            grid[row+i][col+i] -= 1

        ## unmark the "decreasing" diagonals
        hi = min(n - 1 - row, col - 0)
        lo = max(0 - row, col - n + 1)
        for i in range(lo, hi+1):
            if i == 0:
                continue
            grid[row+i][col-i] -= 1
        return

    return backtrack(0, 0)