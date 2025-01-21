# Backtracking Explore Card: https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/

# Attempt 1 that doesn't work / infinite loops. Check notes from 1/21/2025 for ideas on different approach
def soln1(board):
    def backtrack(empties, board):
        if not empties:
            return
        for square in empties:
            candidates = getValidCandidates(square, board)
            if not candidates:
                break
            for candidate in candidates:
                nextEmpties = placeCandidate(candidate, square, empties, board)
                backtrack(nextEmpties, board)
                removeCandidate(square, board)
        return

    def getEmpties(board):
        empties = set()
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empties.add((i,j))
        return empties

    def getValidCandidates(square, board):
        candidates = set([1,2,3,4,5,6,7,8,9])

        def filterByRow(candidates, square, board):
            i, j = square
            cols = []
            if j < 3:
                cols = [3,4,5,6,7,8]
            elif j < 6:
                cols = [0,1,2,6,7,8]
            else:
                cols = [0,1,2,3,4,5]

            for col in cols:
                val = board[i][col]
                if val != "." and int(val) in candidates:
                    candidates.remove(int(val))
            return

        def filterByCol(candidates, square, board):
            i, j = square
            rows = []
            if i < 3:
                rows = [3,4,5,6,7,8]
            elif i < 6:
                rows = [0,1,2,6,7,8]
            else:
                rows = [0,1,2,3,4,5]

            for row in rows:
                val = board[row][j]
                if val != "." and int(val) in candidates:
                    candidates.remove(int(val))
            return

        def filterByBox(candidates, square, board):
            i, j = square
            rows, cols = set(), set()
            if i < 3:
                rows = set([0,1,2])
            elif i < 6:
                rows = set([3,4,5])
            else:
                rows = set([6,7,8])

            if j < 3:
                cols = set([0,1,2])
            elif j < 6:
                cols = set([3,4,5])
            else:
                cols = set([6,7,8])
            
            for row in rows:
                for col in cols:
                    if row == i and col == j:
                        continue
                    val = board[row][col]
                    if val != "." and int(val) in candidates:
                        candidates.remove(int(val))
            return

        filterByRow(candidates, square, board)
        filterByCol(candidates, square, board)
        filterByBox(candidates, square, board)
        return candidates

    def placeCandidate(candidate, square, empties, board):
        i, j = square
        board[i][j] = str(candidate)
        nextEmpties = empties.copy()
        nextEmpties.remove(square)
        return nextEmpties

    def removeCandidate(square, board):
        i, j = square
        board[i][j] = "."
        return

    empties = getEmpties(board)
    backtrack(empties, board)
    return board

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
soln = soln1(board)
print("Solution: " + str(soln))