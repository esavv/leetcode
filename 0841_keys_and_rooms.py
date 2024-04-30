# See: https://leetcode.com/problems/keys-and-rooms/
class Solution(object):
    def canVisitAllRooms(self, rooms):
        return self.soln2(rooms)
        # return self.soln1(rooms)
    
    # approach with a stack
    def soln2(self, rooms):
        visited = [False for _ in range(len(rooms))]
        visited[0] = True
        stack = [0]
        count = 1

        while stack:
            keys = rooms[stack.pop()]
            for key in keys:
                if not visited[key]:
                    stack.append(key)
                    visited[key] = True
                    count += 1
        return count == len(rooms)

    # approach with sets
    def soln1(self, rooms):
        rooms_visited = set([0])
        keys = set(rooms[0])
        rooms_left_to_visit = keys - rooms_visited
        while len(rooms_left_to_visit) > 0:
            room = rooms_left_to_visit.pop()
            rooms_visited.add(room)
            keys = keys.union(rooms[room])
            rooms_left_to_visit = keys - rooms_visited
        return len(rooms) == len(rooms_visited)
        