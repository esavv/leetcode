class Solution(object):
    def reverseWords(self, s):
        return self.soln2(s)
        #return self.soln1(s)

    # 2-pointer approach
    def soln2(self, s):
        start, end = 0, 0
        stack = []
        while start < len(s):
            while start < len(s) and s[start] == ' ':
                start += 1
            end = start
            if start == len(s):
                break

            while end < len(s) and s[end] != ' ':
                end += 1
            stack.append(s[start:end])

            start = end
        
        words = [stack.pop() for _ in range(len(stack))]
        return ' '.join(words)

    # tokenize -> stack -> list
    def soln1(self, s):
        word, stack = [], []
        for c in s:
            if c != ' ':
                word.append(c)
            elif c == ' ' and word:
                stack.append(''.join(word))
                word = []
        if word:
            stack.append(''.join(word))
        
        words = [stack.pop() for _ in range(len(stack))]
        return ' '.join(words)