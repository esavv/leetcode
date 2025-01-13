# returns a list of all k-length subsequences of an n-length array
# a subsequence is a list of distinct indices
# the n-length array is 0-indexed
# 
# time complexity: O(C(n,k)) = O(n! / (k! * (n-k)!))
# this grows "combinatorially", which approaches exponential growth (O(2^n))
# for some values of k but grows more slowly than exponential otherwise
def subseq(n, k):

    # initialize an nXk 2d-array where seqs[i][j] represents the list of j-length
    # subsequences that can be formed beginning from index i to the end of the array
    seqs = []
    for _ in range(n):
        seq = []
        for _ in range(k+1):
            seq.append([])
        seqs.append(seq)

    # define a dynamic programming function that returns the list of j-length
    # subsequences that can be formed beginning from index i to the end of the array
    # this function populates the <seqs> table
    def dp(i, j):
        # terminating conditions:
        if j < 1 or i > n-1 or j > n-i:
            return None

        # memoization check:
        if seqs[i][j]:
            return seqs[i][j]

        # core DP logic
        # save the result into the <seqs> table before returning
        subseqs = dp(i+1, j)
        if subseqs:
            for seq in subseqs:
                seqs[i][j].append(seq)
        subseqs = dp(i+1, j-1)
        if subseqs:
            for seq in subseqs:
                new_seq = [i]
                for val in seq:
                    new_seq.append(val)
                seqs[i][j].append(new_seq)
        else:
            seqs[i][j].append([i])
        return seqs[i][j]

    return dp(0, k)

result = subseq(5, 3)
print("3-length subsequences for 5-length array are: \n" + str(result))