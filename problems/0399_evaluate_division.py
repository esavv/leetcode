# See: https://leetcode.com/problems/evaluate-division/
class Solution(object):
    def calcEquation(self, equations, values, queries):
        return self.soln3(equations, values, queries)
        # return self.soln2(equations, values, queries)
        # return self.soln1(equations, values, queries)

    # graph traversal
    def soln3(self, equations, values, queries):
        # populate the graph
        graph = {}
        for idx, equation in enumerate(equations):
            first, second = equation[0], equation[1]
            if first in graph:
                graph[first].append((second, values[idx]))
            else:
                graph[first] = [(second, values[idx])]
            if second in graph:
                graph[second].append((first, 1.0 / values[idx]))
            else:
                graph[second] = [(first, 1.0 / values[idx])]

        # traverse the graph DFS for each query
        def dfs(start, target, product, visited):
            if start not in graph:
                return -1.0
            if start in graph and start == target:
                return product * 1.0
            for child, value in graph[start]:
                if child not in visited:
                    visited.add(child)
                    result = dfs(child, target, product * value, visited)
                    if result != -1.0:
                        return result
            return -1.0

        answers = [0.0] * len(queries)
        for idx, query in enumerate(queries):
            first, second = query[0], query[1]
            visited = set([first])
            answers[idx] = dfs(first, second, 1.0, visited)
        return answers

    # graph traversal, doesn't work
    def soln2(self, equations, values, queries):
        graph = {}
        # populate the graph
        for idx, equation in enumerate(equations):
            first, second = equation[0], equation[1]
            if first in graph:
                graph[first].append((second, values[idx]))
            else:
                graph[first] = [(second, values[idx])]
            if second in graph:
                graph[second].append((first, 1.0 / values[idx]))
            else:
                graph[second] = [(first, 1.0 / values[idx])]

        variables = {}
        # traverse the graph to populate variables
        def dfs(node):
            for child, value in graph[node]:
                if child not in variables:
                    variables[child] = variables[node] / value
                    dfs(child)
            return

        for equation in equations:
            first = equation[0]
            if first not in variables:
                variables[first] = 1.0
                dfs(first)

        # find the answers from the variables
        answers = [0.0] * len(queries)
        for idx, query in enumerate(queries):
            first, second = query[0], query[1]
            if first not in variables or second not in variables:
                answers[idx] = -1.0
            else:
                answers[idx] = variables[first] / variables[second]
        return answers

    # hash table, doesn't work
    def soln1(self, equations, values, queries):
        variables = {}
        for idx, equation in enumerate(equations):
            first, second = equation[0], equation[1]
            if first in variables and second in variables:
                continue
            if first in variables:
                first_val = variables[first]
                variables[second] = first_val / values[idx]
            elif second in variables:
                second_val = variables[second]
                variables[first] = second_val * values[idx]
            else:
                first_val = 1.0
                second_val = first_val / values[idx]
                variables[first], variables[second] = first_val, second_val

        answers = [0.0] * len(queries)
        for idx, query in enumerate(queries):
            first, second = query[0], query[1]
            if first not in variables or second not in variables:
                answers[idx] = -1.0
            else:
                answers[idx] = variables[first] / variables[second]
        return answers
        