# See: https://leetcode.com/problems/number-of-provinces/
class Solution(object):
    def findCircleNum(self, isConnected):
        return self.soln2(isConnected)
        # return self.soln1(isConnected)
    
    # union find approach, 2/25/2025
    def soln2(self, isConnected):

        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [1] * size
                
            def find(self, x):
                if x == self.root[x]:
                    return x
                self.root[x] = self.find(self.root[x])
                return self.root[x]
            
            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX != rootY:
                    if self.rank[rootX] > self.rank[rootY]:
                        self.root[rootY] = rootX
                    elif self.rank[rootX] < self.rank[rootY]:
                        self.root[rootX] = rootY
                    else:
                        self.root[rootY] = rootX
                        self.rank[rootX] += 1

        n = len(isConnected)
        graph = UnionFind(n)
        for i in range(n-1):
            for j in range(i+1, n):
                if isConnected[i][j] == 1:
                    graph.union(i,j)
        
        for i in range(n):
            graph.find(i)
        
        provinces = set()
        for val in graph.root:
            provinces.add(val)
        return len(provinces)

    # stack approach, 3/14/2024
    def soln1(self, isConnected):
        visited = [False for _ in range(len(isConnected))]
        stack = []
        province_ct = 0
        for i in range(len(isConnected)):
            if visited[i]:
                continue
            stack.append(i)
            visited[i] = True
            while stack:
                city = stack.pop()
                for j in range(len(isConnected)):
                    if not visited[j] and isConnected[city][j]:
                        stack.append(j)
                        visited[j] = True
            province_ct += 1
        return province_ct
