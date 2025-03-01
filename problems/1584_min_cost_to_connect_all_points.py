# See: https://leetcode.com/problems/min-cost-to-connect-all-points/
class Solution(object):
    def minCostConnectPoints(self, points):
        return self.soln1(points)

    # soln #1 from 2/28/2025
    # kruskal's algorithm with optimized union-find
    def soln1(self, points):
        # implement union-find with path compression & union by rank
        class UnionFind:
            def __init__(self, size):
                self.root = [i for i in range(size)]
                self.rank = [1] * size

            def find(self, x):
                if x != self.root[x]:
                    self.root[x] = self.find(self.root[x])
                return self.root[x]

            def union(self, x, y):
                rootX = self.find(x)
                rootY = self.find(y)
                if rootX == rootY:
                    return False

                if self.rank[rootX] > self.rank[rootY]:
                    self.root[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.root[rootX] = rootY
                else:
                    self.root[rootY] = rootX
                    self.rank[rootX] += 1
                return True

        n = len(points)
        edgeCosts = []
        # find the cost of all possible edges
        for i in range(n-1):
            xi, yi = points[i]
            for j in range(i, n):
                xj, yj = points[j]
                cost = abs(xi - xj) + abs(yi - yj)
                edgeCosts.append([cost, i, j])

        # sort by cost ascending
        edgeCosts.sort()

        graph = UnionFind(n)
        totalCost, edgeCount = 0, 0
        # build a minimum spanning tree with kruskal's algorithm
        for cost, i, j in edgeCosts:
            if graph.union(i,j):
                totalCost += cost
                edgeCount += 1
                if edgeCount == n-1:
                    break

        return totalCost