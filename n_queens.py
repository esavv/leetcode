def soln1(self, n):
    #TODO: To manage the queen exploration, we'll use an nXn 2d list to simulate the chessboard
    # We need a way to indicate whether a spot on the board:
    # - has a queen on it
    # - doesn't have a queen, but is under attack by an existing queen
    # - doesn't have a queen and isn't under atack
    # Problem: When we remove a queen on the board and update all of it's "under attack" spaces, we
    #   need to be careful to not accidentally erase the "under attack" status of a space that's still
    #   under attack by another queen that's not being removed
    # One way to do this: Initialize the grid to zeros, and increment a space by 1 every time it becomes
    #   under attack by a new queen. Decrement whenever an attacking queen is removed
    # Since the integers 0 up until n are reserved for safe spaces and spaces under attack, we can mark
    #   a space with a queen using anything other than these values. Perhaps -1 will suffice.

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
        return True

    def place_queen(row, col):
        return

    def remove_queen(row, col):
        return

    return backtrack(0, 0)