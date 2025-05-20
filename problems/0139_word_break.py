# See: https://leetcode.com/problems/word-break/
class Solution(object):
    def wordBreak(self, s, wordDict):
        return self.soln1(s, wordDict)
        
    # soln #1 on 5/20/2025
    # backtracking, time limit exceeded
    def soln1(self, s, wordDict):
        n = len(s)
        seqs = []
        wordDictSet = set(wordDict)

        def backtrack(k, seq, start):
            if seqs:
                return
            if k == 1:
                if s[start:] in wordDictSet:
                    seq.append(s[start:])
                    seqs.append(list(seq))
                    seq.pop()
            else:
                for i in range(start+1, n-k+2):
                    if s[start:i] in wordDictSet:
                        seq.append(s[start:i])
                        backtrack(k-1, seq, i)
                        seq.pop()
            return

        for k in range(1, n+1):
            seqs = []
            backtrack(k, [], 0)
            if seqs:
                return True
        return False