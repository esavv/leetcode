# See: https://leetcode.com/problems/simplify-path/
class Solution(object):
    def simplifyPath(self, path):
        return self.soln1(path)
    
    # soln #1 on 4/20/2025
    # stack
    def soln1(self, path):
        rawFiles = path.split("/")
        cleanFiles = [file for file in rawFiles if file != '']

        stack = []
        for file in cleanFiles:
            if file == ".":
                continue
            elif file == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(file)

        pathList = []
        for file in stack:
            pathList.append('/')
            pathList.append(file)
        if not pathList:
            pathList = ['/']
        
        simplifiedPath = ''.join(pathList)
        return simplifiedPath