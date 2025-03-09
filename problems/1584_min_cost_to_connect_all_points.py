# See: https://leetcode.com/problems/min-cost-to-connect-all-points/
class Solution(object):
    def minCostConnectPoints(self, points):
        return self.soln2(points)
        # return self.soln1(points)

    # soln #1 from 3/08/2025
    # prim's algorithm
    def soln2(self, points):
        n = len(points)
        graph = [[0] * n for _ in range(n)]
        for i in range(n-1):
            for j in range(i+1, n):
                weight = abs(points[i][0] - points[j][0]) + abs(points[i][1] - points[j][1])
                graph[i][j] = graph[j][i] = weight

        unvisited = set([i for i in range(1, n)])
        cost = 0

        heap = []
        for point in unvisited:
            weight = graph[0][point]
            heap.append([weight, point])
        import heapq
        heapq.heapify(heap)

        while unvisited:
            weight, pointA = heapq.heappop(heap)
            while pointA not in unvisited:
                weight, pointA = heapq.heappop(heap)

            cost += weight
            unvisited.remove(pointA)

            for pointB in unvisited:
                weight = graph[pointA][pointB]
                heapq.heappush(heap, [weight, pointB])
        return cost

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