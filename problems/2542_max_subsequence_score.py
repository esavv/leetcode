# See: https://leetcode.com/problems/maximum-subsequence-score/
import heapq
class Solution(object):
    def maxScore(self, nums1, nums2, k):
        return self.soln2(nums1, nums2, k)
        # return self.soln1(nums1, nums2, k)

    # sorting + heap + sliding window
    def soln2(self, nums1, nums2, k):
        n = len(nums1)
        for i in range(n):
            nums1[i] = (nums1[i], nums2[i])

        nums1.sort(key=lambda tup: tup[1], reverse=True)
        heap, currSum = [], 0

        for i in range(k):
            heap.append(nums1[i][0])
            currSum += nums1[i][0]
        maxScore = currSum * nums1[k-1][1]
        heapq.heapify(heap)

        for i in range(k, n):
            currSum -= heapq.heappop(heap)
            heapq.heappush(heap, nums1[i][0])
            currSum += nums1[i][0]
            maxScore = max(maxScore, currSum * nums1[i][1])

        return maxScore

    # brute force, combinatorial time complexity ( O(C(n,k)) )
    def soln1(self, nums1, nums2, k):
        n = len(nums1)

        seqs = []
        for _ in range(n):
            seq = []
            for _ in range(k+1):
                seq.append([])
            seqs.append(seq)
        def dp(i, j):
            if j < 1 or i > n-1 or j > n-i:
                return None

            if seqs[i][j]:
                return seqs[i][j]

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

        subseqs = dp(0, k)

        max1 = float("-inf")
        for subseq in subseqs:
            sum1 = 0
            min2 = float("inf")
            for idx in subseq:
                sum1 += nums1[idx]
                min2 = min(min2, nums2[idx])
            score = sum1 * min2
            max1 = max(max1, score)
        return max1