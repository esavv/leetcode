# See: https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
from collections import deque
class Solution(object):
    def minReorder(self, n, connections):
        return self.soln2(n, connections)
        # return self.soln1(n, connections)

    # attempt without using nodes
    def soln2(self, n, connections):
        cities = {}
        for i in range(n):
            cities[i] = ([],[])
        for connection in connections:
            fro, to = connection[0], connection[1]
            cities[fro][0].append(to)
            cities[to][1].append(fro)
        visited = set()
        ans = 0
        lqueue, rqueue = deque([0]), deque()
        while lqueue or rqueue:
            while lqueue:
                root = lqueue.popleft()
                visited.add(root)
                for idx in cities[root][0]:
                    if idx not in visited:
                        rqueue.append(idx)
                        ans += 1
                for idx in cities[root][1]:
                    if idx not in visited:
                        rqueue.append(idx)

            while rqueue:
                root = rqueue.popleft()
                visited.add(root)
                for idx in cities[root][0]:
                    if idx not in visited:
                        lqueue.append(idx)
                        ans += 1
                for idx in cities[root][1]:
                    if idx not in visited:
                        lqueue.append(idx)
        return ans

    # convert edges to node tree + BFS; linear time & space
    def soln1(self, n, connections):
        cities = []
        for _ in range(n):
            cities.append(Node())
        for connection in connections:
            fro, to = connection[0], connection[1]
            cities[fro].outbound.append(cities[to])
            cities[to].inbound.append(cities[fro])
        root = cities[0]
        visited = set()
        ans = 0
        lqueue, rqueue = deque(), deque()
        lqueue.append(root)
        while lqueue or rqueue:
            while lqueue:
                root = lqueue.popleft()
                visited.add(root)
                for node in root.outbound:
                    if node not in visited:
                        rqueue.append(node)
                        ans += 1
                for node in root.inbound:
                    if node not in visited:
                        rqueue.append(node)

            while rqueue:
                root = rqueue.popleft()
                visited.add(root)
                for node in root.outbound:
                    if node not in visited:
                        lqueue.append(node)
                        ans += 1
                for node in root.inbound:
                    if node not in visited:
                        lqueue.append(node)
        return ans        

class Node(object):
    def __init__(self):
        self.inbound = []
        self.outbound = []
