# See: 
class Solution(object):
    def reverseVowels(self, s):
        return self.soln4(s)    
        #return self.soln3(s)
        #return self.soln2(s)
        #return self.soln1(s)

    # soln3 but in one pass
    def soln4(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, len(s) - 1
        ans = list(s)
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                ans[i], ans[j] = s[j], s[i]
                i += 1
                j -= 1
            else:
                if s[i] not in vowels:
                    i += 1
                if s[j] not in vowels:
                    j -= 1
        return ''.join(ans)

    # string manipulation efficiencies
    def soln3(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        ansl = list(s)
        chars = []
        for c in ansl:
            if c in vowels:
                chars.append(c)
        j = len(chars) - 1
        for i, c in enumerate(ansl):
            if c in vowels:
                ansl[i] = chars[j]
                j -= 1
        return ''.join(ansl)

    # minor time & space improvements
    def soln2(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        i, j = 0, len(s) - 1
        start, end = '', ''
        while i < j:
            if s[i] in vowels and s[j] in vowels:
                start = start + s[j]
                end = s[i] + end
                i += 1
                j -= 1
            else:
                if s[i] not in vowels:
                    start = start + s[i]
                    i += 1
                if s[j] not in vowels:
                    end = s[j] + end
                    j -= 1
        if i == j:
            start = start + s[i]
        return start + end

    # two passes & lots of string inefficiencies
    def soln1(self, s):
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        ansl = list(s)
        chars = []
        for c in ansl:
            if c in vowels:
                chars.append(c)
        j = len(chars) - 1
        ans = ''
        for i, c in enumerate(ansl):
            if c in vowels:
                ansl[i] = chars[j]
                j -= 1
            ans += ansl[i]
        return ans
