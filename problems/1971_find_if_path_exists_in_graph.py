# See: https://leetcode.com/problems/find-if-path-exists-in-graph/
class Solution(object):
    def validPath(self, n, edges, source, destination):
        return self.soln2(n, edges, source, destination)
        # return self.soln1(n, edges, source, destination)

    # soln #2 from 2/27/2025
    # iterative BFS
    def soln2(self, n, edges, source, destination):
        from collections import deque

        # edge case
        if source == destination:
            return True

        # build graph from edges
        graph = {}
        for i in range(n):
            graph[i] = []
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        queue = deque([source])
        visited = set([source])
        while queue:
            node = queue.popleft()
            for child in graph[node]:
                if child == destination:
                    return True
                if child not in visited:
                    queue.append(child)
                    visited.add(child)
        return False

    # soln #1 from 2/27/2025
    # iterative DFS
    def soln1(self, n, edges, source, destination):
        # edge case
        if source == destination:
            return True

        # build graph from edges
        graph = {}
        for i in range(n):
            graph[i] = []
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
            
        # DFS the graph starting at source
        stack = [source]
        visited = set([source])
        while stack:
            node = stack.pop()
            for child in graph[node]:
                if child == destination:
                    return True
                if child not in visited:
                    stack.append(child)
                    visited.add(child)
        return False