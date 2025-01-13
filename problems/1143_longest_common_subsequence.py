# See: https://leetcode.com/problems/longest-common-subsequence/
class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        return self.soln4(text1, text2)
        # return self.soln3(text1, text2)
        # return self.soln2(text1, text2)
        # return self.soln1(text1, text2)

    # with hint: dynamic programming formulated in terms of LCS, with memoization
    def soln4(self, text1, text2):
        # remove non-overlapping chars from both strings
        # this optimization reduces worst-case DP inputs (no common subsequence)
        #   to linear time execution, and speeds up performance for average/best cases
        text1_chars = set([char for char in text1])
        text2_chars = set([char for char in text2])
        text1_adj, text2_adj = "", ""

        for char in text1:
            if char in text2_chars:
                text1_adj += char
        for char in text2:
            if char in text1_chars:
                text2_adj += char

        text1, text2 = text1_adj, text2_adj
 
        n, m = len(text1), len(text2)
        seqs = [[0 for _ in range(m)] for _ in range(n)]

        def dp(i, j):
            if i == -1 or j == -1:
                return 0
            if seqs[i][j]:
                return seqs[i][j]
            
            if text1[i] == text2[j]:
                seqs[i][j] = dp(i-1, j-1) + 1
                return seqs[i][j]
            left, up = dp(i-1, j), dp(i, j-1)
            if left > up:
                seqs[i][j] = left
            else:
                seqs[i][j] = up
            return seqs[i][j]

        return dp(n-1, m-1)

    # remove all non-overlapping chars linearly before dynamic programming
    def soln3(self, text1, text2):
        text1_chars = set([char for char in text1])
        text2_chars = set([char for char in text2])
        text1_adj, text2_adj = "", ""

        for char in text1:
            if char in text2_chars:
                text1_adj += char
        for char in text2:
            if char in text1_chars:
                text2_adj += char

        if not text1_adj or not text2_adj:
            return 0

        n, m = len(text1_adj), len(text2_adj)
        k = min(n, m)

        def subseq(text, k, idx, seqs):
            if k <= 0:
                return set([""])
            if idx >= len(text):
                return set()
            if k > len(text) - idx:
                return set()
            if seqs[k][idx]:
                return seqs[k][idx]

            for seq in subseq(text, k, idx+1, seqs):
                seqs[k][idx].add(seq)
            # save some space
            if k > 0 and idx+1 < len(text):
                seqs[k][idx+1] = None
            
            for seq in subseq(text, k-1, idx+1, seqs):
                new_seq = text[idx] + seq
                seqs[k][idx].add(new_seq)

            return seqs[k][idx]

        def overlap(set1, set2):
            for item in set1:
                if item in set2:
                    return True
            return False

        seqs1 = [[set() for _ in range(n)] for _ in range(k+1)]
        seqs2 = [[set() for _ in range(m)] for _ in range(k+1)]
        while k > 0:
            if overlap(subseq(text1_adj, k, 0, seqs1), subseq(text2_adj, k, 0, seqs2)):
                return k 
            k -= 1
        return 0

    # calculate subsequences recursively with memoization
    def soln2(self, text1, text2):
        n, m = len(text1), len(text2)
        k = min(n, m)

        def subseq(text, k, idx, seqs):
            if k <= 0:
                return set([""])
            if idx >= len(text):
                return set()
            if k > len(text) - idx:
                return set()
            if seqs[k][idx]:
                return seqs[k][idx]

            for seq in subseq(text, k, idx+1, seqs):
                seqs[k][idx].add(seq)
            
            for seq in subseq(text, k-1, idx+1, seqs):
                new_seq = text[idx] + seq
                seqs[k][idx].add(new_seq)

            return seqs[k][idx]

        def overlap(set1, set2):
            for item in set1:
                if item in set2:
                    return True
            return False

        seqs1 = [[set() for _ in range(n)] for _ in range(k+1)]
        seqs2 = [[set() for _ in range(m)] for _ in range(k+1)]
        while k > 0:
            if overlap(subseq(text1, k, 0, seqs1), subseq(text2, k, 0, seqs2)):
                return k 
            k -= 1
        return 0

    # calculate subsequences recursively
    def soln1(self, text1, text2):
        def getSubsequences(text, start_idx, seq_len, seqs, seq):
            for idx in range(start_idx, len(text) - seq_len + 1):
                # hack to prune recursion for repeated chars
                if idx > start_idx and text[idx] == text[idx-1]:
                    continue
                new_seq = seq + text[idx]
                if seq_len == 1:
                    seqs.add(new_seq)
                else:
                    getSubsequences(text, idx+1, seq_len-1, seqs, new_seq)

        def overlap(set1, set2):
            for item in set1:
                if item in set2:
                    return True
            return False

        seq_len = min(len(text1), len(text2))
        while seq_len > 0:
            set1, set2 = set(), set()
            getSubsequences(text1, 0, seq_len, set1, "")
            getSubsequences(text2, 0, seq_len, set2, "")
            if overlap(set1, set2):
                return seq_len 
            seq_len -= 1
        return 0
        