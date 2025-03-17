# See: https://leetcode.com/problems/daily-temperatures/
class Solution(object):
    def dailyTemperatures(self, temperatures):
        return self.soln2(temperatures)
        # return self.soln1(temperatures)

    # soln #2 from 3/17/2025
    # stack + backwards traversal
    def soln2(self, temperatures):
        n = len(temperatures)
        answer = [0] * n
        stack = [n-1]

        for i in range(n-2, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                answer[i] = stack[-1] - i

            stack.append(i)

        return answer

    # soln #1 from 3/17/2025
    # brute force
    def soln1(self, temperatures):
        n = len(temperatures)
        answer = [0] * n

        for i in range(n-1):
            for j in range(i,n):
                if temperatures[j] > temperatures[i]:
                    answer[i] = j - i
                    break

        return answer
    